import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:600
    height:400
    title:'slider'


    Column {
        anchors.centerIn:parent
        spacing:40

        Label {
            id:mylabel
            text:'Hello'
            font.pixelSize:22
            font.bold:true

        }

        Slider{
            id:slider
            from:0
            value:25
            to:100

            onMoved:
            {
            mylabel.text = slider.value
            }
        }
    }
}