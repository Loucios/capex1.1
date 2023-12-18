from openpyxl import load_workbook


def main():
    filename = 'capex.xlsx'
    wb = load_workbook(filename=filename)


if __name__ == '__main__':
    main()
