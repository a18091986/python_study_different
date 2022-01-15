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

    ScatterSeries {
        id:scatter1
        name:'Scatter 1'
        XYPoint {x:1.5; y:1.5}
        XYPoint {x:1.5; y:1.6}
        XYPoint {x:1.57; y:1.55}
        XYPoint {x:1.8; y:1.6}
        XYPoint {x:2.5; y:1.3}
    }

    ScatterSeries {
        id:scatter2
        name:'Scatter 2'
        XYPoint {x:2.0; y:2.1}
        XYPoint {x:2.5; y:2.6}
        XYPoint {x:2.57; y:2.55}
        XYPoint {x:1.8; y:2.6}
        XYPoint {x:2.5; y:2.1}
    }
 }



}
