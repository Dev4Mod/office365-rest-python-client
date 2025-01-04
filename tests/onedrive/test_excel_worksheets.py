from office365.onedrive.driveitems.driveItem import DriveItem
from office365.onedrive.workbooks.worksheets.protection_options import (
    WorkbookWorksheetProtectionOptions,
)
from office365.onedrive.workbooks.worksheets.worksheet import WorkbookWorksheet
from tests import create_unique_name
from tests.graph_case import GraphTestCase
from tests.onedrive.test_excel import upload_excel


class TestExcelWorksheets(GraphTestCase):
    excel_file = None  # type: DriveItem
    sheet_name = create_unique_name("Sheet")
    worksheet = None  # type: WorkbookWorksheet

    @classmethod
    def setUpClass(cls):
        super(TestExcelWorksheets, cls).setUpClass()
        cls.excel_file = upload_excel(cls.client.me.drive)
        assert cls.excel_file.resource_path is not None

    @classmethod
    def tearDownClass(cls):
        cls.excel_file.delete_object().execute_query_retry()

    def test1_add_worksheet(self):
        result = self.__class__.excel_file.workbook.worksheets.add(
            self.sheet_name
        ).execute_query()
        self.assertIsNotNone(result.resource_path)

    def test2_list_worksheets(self):
        result = self.__class__.excel_file.workbook.worksheets.get().execute_query()
        self.assertIsNotNone(result.resource_path)
        self.assertGreaterEqual(len(result), 1)
        self.__class__.worksheet = result[0]

    def test3_used_range(self):
        result = self.__class__.worksheet.used_range().execute_query()
        self.assertIsNotNone(result.address)

    def test4_protect_worksheet(self):
        ws = self.__class__.worksheet
        options = WorkbookWorksheetProtectionOptions(allowDeleteRows=False)
        ws.protection.protect(options).execute_query()
        result = ws.protection.get().execute_query()
        self.assertFalse(result.options.allowDeleteRows)

    def test5_delete_worksheet(self):
        worksheet = self.__class__.excel_file.workbook.worksheets[self.sheet_name]
        worksheet.delete_object().execute_query()
