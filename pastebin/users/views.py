import csv
import xlwt


from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpResponse

User = get_user_model()


def export_stat_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Statistics.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Num of Pastes'])

    users = User.objects.all().annotate(Count('pastes')).values_list('username', 'pastes__count')

    for user in users:
        writer.writerow(user)

    return response


def export_stat_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Statistics.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Statistics')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'Num of Pastes']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().annotate(Count('pastes')).values_list('username', 'pastes__count')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
