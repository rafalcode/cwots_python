#!/usr/bin/env python3
###############################################################################
#
# Example of how to add conditional formatting to an XlsxWriter file.
#
# Conditional formatting allows you to apply a format to a cell or a
# range of cells based on certain criteria.
#
# SPDX-License-Identifier: BSD-2-Clause
# Copyright 2013-2023, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter

workbook = xlsxwriter.Workbook("conditional_format.xlsx")
# we will have 9 sokrsheets because there are 9 examples.
worksheet8 = workbook.add_worksheet()
worksheet9 = workbook.add_worksheet()

# Add a format. Light red fill with dark red text.
format1 = workbook.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006"})

# Add a format. Green fill with dark green text.
format2 = workbook.add_format({"bg_color": "#C6EFCE", "font_color": "#006100"})

# Some sample data to run the conditional formatting against.
data = [
    [34, 72, 38, 30, 75, 48, 75, 66, 84, 86],
    [6, 24, 1, 84, 54, 62, 60, 3, 26, 59],
    [28, 79, 97, 13, 85, 93, 93, 22, 5, 14],
    [27, 71, 40, 17, 18, 79, 90, 93, 29, 47],
    [88, 25, 33, 23, 67, 1, 59, 79, 47, 36],
    [24, 100, 20, 88, 29, 33, 38, 54, 54, 88],
    [6, 57, 88, 28, 10, 26, 37, 7, 41, 48],
    [52, 78, 1, 96, 26, 45, 47, 33, 96, 36],
    [60, 54, 81, 66, 81, 90, 80, 93, 12, 55],
    [70, 5, 46, 14, 71, 19, 66, 36, 41, 21],
]

###############################################################################
#
# Example 8.
#
caption = "Examples of data bars."

worksheet8.write("A1", caption)

worksheet8.write("B2", "Default data bars")
worksheet8.write("D2", "Bars only")
worksheet8.write("F2", "With user color")
worksheet8.write("H2", "Solid bars")
worksheet8.write("J2", "Right to left")
worksheet8.write("L2", "Excel 2010 style")
worksheet8.write("N2", "Negative same as positive")

data = range(1, 13)
for row, row_data in enumerate(data):
    worksheet8.write(row + 2, 1, row_data)
    worksheet8.write(row + 2, 3, row_data)
    worksheet8.write(row + 2, 5, row_data)
    worksheet8.write(row + 2, 7, row_data)
    worksheet8.write(row + 2, 9, row_data)

data = [-1, -2, -3, -2, -1, 0, 1, 2, 3, 2, 1, 0]
for row, row_data in enumerate(data):
    worksheet8.write(row + 2, 11, row_data)
    worksheet8.write(row + 2, 13, row_data)

worksheet8.conditional_format("B3:B14", {"type": "data_bar"})

worksheet8.conditional_format("D3:D14", {"type": "data_bar", "bar_only": True})

worksheet8.conditional_format("F3:F14", {"type": "data_bar", "bar_color": "#63C384"})

worksheet8.conditional_format("H3:H14", {"type": "data_bar", "bar_solid": True})

worksheet8.conditional_format("J3:J14", {"type": "data_bar", "bar_direction": "right"})

worksheet8.conditional_format("L3:L14", {"type": "data_bar", "data_bar_2010": True})

worksheet8.conditional_format(
    "N3:N14",
    {
        "type": "data_bar",
        "bar_negative_color_same": True,
        "bar_negative_border_color_same": True,
    },
)

workbook.close()
