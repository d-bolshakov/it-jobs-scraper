from datetime import date, datetime


def convertDate(dateStr: str) -> date:
    split = dateStr.rsplit(" ")
    day = split[0]
    month = ''
    year = split[2]
    match split[1]:
        case 'січня':
            month = '01'
        case 'лютого':
            month = '02'
        case 'березня':
            month = '03'
        case 'квітня':
            month = '04'
        case 'травня':
            month = '05'
        case 'червня':
            month = '06'
        case 'липня':
            month = '07'
        case 'серпня':
            month = '08'
        case 'вересня':
            month = '09'
        case 'жовтня':
            month = '10'
        case 'листопада':
            month = '11'
        case 'грудня':
            month = '12'
    return datetime.strptime(year + '-' + month + '-' + day, '%Y-%m-%d').date()
