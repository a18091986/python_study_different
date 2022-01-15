import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:600
    height:400
    title:'menubar'

    menuBar: MenuBar {

        Menu {
            title:'File'
            Action {text:'New'}
            Action {text:'Save'}
            Action {text:'Save As'}
        }
        Menu {
            title:'Edit'
            Action {text:'Cut'}
            Action {text:'Copy'}
            Action {text:'Paste'}
        }
        Menu {
            title:'Help'
            Action {text:'About'}
             }
    }


}