import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:600
    height:400
    title:'CheckBox'

    Column {

    anchors.centerIn:parent
    spacing:20

    CheckBox{

        checked:true
        text:'Python'

    }
    CheckBox{

        checked:true
        text:'Java'

    }
    CheckBox{

        checked:false
        text:'C++'

    }
    }


}