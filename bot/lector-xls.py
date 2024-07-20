'''
Library_xlrd documentation IS DEPRECATED
https://xlrd.readthedocs.io/en/latest/genindex.html
'''
import xlrd
from xlutils.copy import copy


# TODO: Error al agregar hoja de por medio.

# Use methods in flask_app.py
# -num_hojas()
# -filas_column()
# -cell_info()
# -col_info()
# -id_find_xls()
# -show_cols()
# -matriz_sheet()

# NAMEBOOK = '/home/Piztecho/mysite/'
NAMEBOOK = ''
workbook = 'pagina.xls'
book = xlrd.open_workbook(NAMEBOOK+workbook, formatting_info=True)
number_sheets = book.nsheets  # Numero de hojas que tiene el libro de excel


def edit_cell(num_sheet, rowx, coly, new_value):
    book_editable = copy(book)
    sheet = book_editable.get_sheet(num_sheet)
    sheet.write(rowx, coly, new_value)
    book_editable.save(workbook)

# edit_cell(0, 0,0,'Prueba')


def num_hojas(file):
    book = xlrd.open_workbook(NAMEBOOK+file)
    number_sheets = book.nsheets  # Numero de hojas que tiene el libro de excel
    return number_sheets


def filas_column(file, page):
    book = xlrd.open_workbook(NAMEBOOK+file)
    return book.sheet_by_index(page).nrows, book.sheet_by_index(page).ncols


def cell_info(file, page, rowX, colY):
    book = xlrd.open_workbook(NAMEBOOK+file)
    return book.sheet_by_index(page).cell_value(rowX, colY)


def col_info(file, page, col):
    book = xlrd.open_workbook(NAMEBOOK+file)
    return book.sheet_by_index(page).col_values(col)


def id_find_xls(file, page, id):
    book = xlrd.open_workbook(NAMEBOOK+file)
    try:
        sheet = book.sheet_by_index(page)  # load 0 page

        id_index = sheet.row_values(0).index("id")
        if id in sheet.col_values(id_index):
            print("Id encontrada en hoja\t", sheet)
            return id_index, True
        else:
            print("Id en columna: NO Encontrado", sheet)
            return 0, False
    except ValueError as e:
        print('Error type: ', type(e))
        print("-----------------------\n")


def show_cols(file, page, cols):
    book = xlrd.open_workbook(NAMEBOOK+file)
    sheet = book.sheet_by_index(page)
    index_cols = [int(col) for col in cols.split(',')]
    cols_value = []
    for index in index_cols:
        cols_value.append(sheet.col_values(index))
    return cols_value
    # for column in cols:


def matriz_sheet(file, page):
    book = xlrd.open_workbook(NAMEBOOK+file)
    sheet = book.sheet_by_index(page)
    return [sheet.row_values(row) for row in range(sheet.nrows)]


def find_column(id, page):
    try:
        sheet = book.sheet_by_index(page)  # load 0 page
        # busca el indice de la columna id
        id_index = sheet.row_values(0).index("id")
        # En caso de no estar la palabra id en la fila retorna una lista vacia.
        # Busca que el id esté en los valores de la columna si no está retorna una
        # lista vacía, si está retorna el valor de la columna donde se escuentra.
        if id in sheet.col_values(id_index):
            print("Id encontrada en hoja\t", sheet)
            # print("-----------------------\n")
            return id_index, True
        else:
            print("Id en columna: NO Encontrado", sheet)
            return 0, False
        # elif id_index.type
    except ValueError as e:
        print('Error type: ', type(e))
        print("-----------------------\n")


def next_aproved(row, column, page):
    actual_page = book.sheet_by_index(page)  # load 0 page
    # Primero comprobar que el valor de la siguiente columna sea booleano.
    if actual_page.ncols > 1:

        # EL VALOR TRUE O FALSE los puede leer como strings
        its_boolean = str(actual_page.cell(row, column+1).value)
        # revisar a atras y adelante
        if its_boolean.lower() == "true":
            return True
        elif its_boolean.lower() == "false":
            # print("Valor booleano:", its_boolean)
            return False
        else:
            print("Busca el valor true o false en otra columna :)\n")
            return "No booleano"
    else:
        print("No existe columnas por revisar")


def load_XLRD(id_search):
    try:
        # recorre la cantidad total de paginas
        for index_page in range(number_sheets):  # recorre cada pagina
            actual_page = book.sheet_by_index(index_page)
            # Busca la columna que contene el id
            index_id, find = find_column(id_search, index_page)
            if find:  # Si se encontró el id prosigue
                row_index = actual_page.col_values(index_id).index(id_search)
                print("Celda y fila:", xlrd.formula.cellname(row_index, index_id))
                print("-----------------------\n")
                # Si tiene su evaluador booleano prosigue
                if next_aproved(row_index, index_id, index_page) == "No booleano":
                    print("-----------------------\n")
                elif next_aproved(row_index, index_id, index_page):
                    print("DATOS DE: ", actual_page.row_values(row_index), "\n")
                    print("-----------------------\n")
            else:
                print("-----------------------\n")
    except ValueError as e:
        print('Error type: ', type(e))

# def validation( password):
#     salt =

# load_XLRD(4)