import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:600
    height:400
    title:'spinbox'


    Column {
        anchors.centerIn:parent
        spacing:40

        Label {
            id:mylabel
            text:'Hello'
            font.pixelSize:22
            font.bold:true

        }

        SpinBox{
            id:spinbox
            from:0
            value:100
            to:100*100
            stepSize:100

            onValueModified:

            {mylabel.text = 'Selected value is: ' + spinbox.displayText}

        }
    }
}