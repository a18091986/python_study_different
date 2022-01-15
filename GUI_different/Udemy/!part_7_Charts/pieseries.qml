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

    }

    PieSeries {

        id:pieseries
        PieSlice {label:'Python'; value:90}
        PieSlice {label:'C++'; value:80}
        PieSlice {label:'Java'; value:60}
        PieSlice {label:'C#'; value:40}

    }

}
