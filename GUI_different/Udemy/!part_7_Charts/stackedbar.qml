import QtQuick 2.5
import QtQuick.Controls 2.5
import QtCharts 2.5

ApplicationWindow{

    visible:true
    width:600
    height:600
    title:"LineChart"

    ChartView {

        anchors.fill:parent
        antialiasing:true
        theme:ChartView.ChartThemeDark

    StackedBarseries {
        id:myseries
        axisX: BarCategoryAxis {categories: ['2016', '2017', '2018', '2019', '2020', '2021']}
        BarSet {label : 'Parwiz'; values:[2,2,3,4,5,6]}
        BarSet {label : 'John'; values:[5,2,3,5,5,6]}
        BarSet {label : 'Bob'; values:[3,5,8,13,5,6]}
    }
}
}