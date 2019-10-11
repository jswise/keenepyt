"""Define the ExKML class."""

import os
import xml.etree.ElementTree as ET

import arcpy
from arcpy.da import SearchCursor # pylint: disable=no-name-in-module
from arcpy.da import UpdateCursor # pylint: disable=no-name-in-module

from keenepyt.core.thing import Thing

class ExKML(Thing):
    """Represents a feature class containing data that used to be in a KML file."""

    fc = None

    def __init__(self, fc, helpers=None, **kwargs):
        super().__init__(helpers, **kwargs)
        self.fc = fc

    def extract_popup_info(self):
        """Extract data from the PopupInfo field to new fields."""

        # Make sure we have a feature class with a PopupInfo field.
        if not arcpy.Exists(self.fc):
            self.raise_error('Feature class {} not found.'.format(self.fc))
        popup_field_name = 'PopupInfo'
        if not self.field_exists(popup_field_name):
            self.raise_error('No {} field found in {}.'.format(popup_field_name, self.fc))

        # Find out what fields are in the popup.
        search_cursor = SearchCursor(self.fc, popup_field_name)
        first_row = search_cursor.next()
        sample_html = first_row[0]
        popup_dict = self.get_popup_dict(sample_html)
        popup_fields = list(popup_dict.keys())
        del first_row
        del search_cursor

        # Add new fields as necessary.
        fc_name = os.path.basename(self.fc)
        for field_name in popup_fields:
            if not self.field_exists(field_name):
                self.info('Adding field "{}" to {}.'.format(field_name, fc_name))
                try:
                    arcpy.management.AddField(self.fc, field_name, 'TEXT')
                except Exception as e:
                    self.raise_error('Failed to add field. {}'.format(e))

        # Populate the fields.
        self.info('Updating attributes.')
        update_fields = popup_fields + [popup_field_name]
        cursor = UpdateCursor(self.fc, update_fields)
        for row in cursor:
            popup_html = row[-1]
            popupdict = self.get_popup_dict(popup_html)
            for field_index, field_name in enumerate(popup_fields):
                row[field_index] = popupdict.get(field_name, None)
            cursor.updateRow(row)
        del cursor

    def field_exists(self, field_name):
        """See if a field exists in the feature class.

        :param field_name: The field the check

        :return: Boolean indicating if field exists
        """

        fields = arcpy.ListFields(self.fc, field_name)
        field_count = len(fields)
        return (field_count == 1)

    def get_popup_dict(self, popup_html):
        """Convert popup HTML code into a dictionary.

        :param popup_html: The HTML from a popup attribute in a feature class

        :return: A dictionary containing the popup information
        """

        # Fix HTML that doesn't include the "body" tag.
        if '<body' not in popup_html:
            popup_html = '<body>' + popup_html + '</body>'

        # Load the important part into an ElementTree object.
        body_start = popup_html.find('<body')
        body_end = popup_html.find('</body>')
        body_text = popup_html[body_start:body_end + 7]
        body_text = body_text.replace('<Null>', '')
        body_text = body_text.replace('&', '&amp;')
        try:
            body_element = ET.fromstring(body_text)
        except Exception as e:
            self.raise_error('Failed to load HTML. {}'.format(e))

        # If the table contains any subtables, use the first one.
        table = body_element.findall('table')[0]
        row = table.findall('tr')[1]
        column = row.findall('td')[0]
        subtables = column.findall('table')
        if len(subtables) > 0:
            table = subtables[0]
        
        # Convert the table to a dictionary.
        rows = table.findall('tr')
        popup_dict = {}
        for row in rows:
            columns = row.findall('td')
            raw_key = columns[0].text
            key = str(raw_key).replace(' ', "_")
            bold = columns[1].findall('b')
            if len(bold) > 0:
                raw_val = bold[0].text
            else:
                raw_val = columns[1].text
            if raw_val is None:
                raw_val = ''
            val = str(raw_val).replace('"', "'")
            popup_dict[key] = val

        return popup_dict
