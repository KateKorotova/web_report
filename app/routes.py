from flask import Blueprint, render_template, request, redirect, url_for
from racing_report.build_report import build_report

bp = Blueprint('main', __name__, template_folder='templates')
DATA_FOLDER = "app/data/"


@bp.route('/')
def index():
    return redirect(url_for('main.report'))


@bp.route('/report/')
def report():
    order = request.args.get('order', 'asc')
    order = request.args.get('order', 'asc') if request.args.get('order', 'asc') else 'asc'
    sort_asc = order == 'asc'
    report_data = build_report(DATA_FOLDER)
    sorted_report = report_data.sort_values(by='lap_time', ascending=sort_asc)
    return render_template('report.html', report=sorted_report, order=order)


@bp.route('/report/drivers/')
def drivers():
    driver_id = request.args.get('driver_id')
    order = request.args.get('order', 'asc')
    sort_asc = order == 'asc'
    report_data = build_report(DATA_FOLDER).sort_values(
        by='abbr_driver', ascending=sort_asc)

    if driver_id:
        driver_data = report_data[report_data['abbr_driver'] == driver_id]
        if driver_data.empty:
            return "Driver ID not found", 404
        return render_template('driver_info.html', driver=driver_data)
    else:
        drivers_list = report_data[['abbr_driver', 'driver']].sort_values(
            by='driver', ascending=sort_asc)
        return render_template('drivers.html', drivers=drivers_list, order=order)
