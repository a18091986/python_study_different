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

        LineSeries {

            name:"LineSeries"
            XYPoint {x:0; y:0}
            XYPoint {x:1.1; y:2.1}
            XYPoint {x:1.9; y:2.5}
            XYPoint {x:2.1; y:3.1}
            XYPoint {x:3.4; y:4.2}
            XYPoint {x:4.3; y:3.1}


        }

    }
}