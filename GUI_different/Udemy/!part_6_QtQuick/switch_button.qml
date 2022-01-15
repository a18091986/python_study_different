import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:600
    height:400
    title:'scrollview'

    Column {
        anchors.centerIn:parent
        spacing:20
        Switch {

            text:'Wi-Fi'

        }
        Switch {

            text:'Bluetooth'

        }
    }


}