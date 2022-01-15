import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:600
    height:400
    title:'Combobox'

    Column{
        anchors.centerIn:parent
        spacing: 40

        Label {

            id:mylabel
            text:'Hello'
            font.pixelSize:22
            font.bold:true

        }


        ComboBox {
            id:combo
            font.pixelSize:22
            model:['Python', 'Java', 'C++']

            onActivated: {
                mylabel.text = 'You have selected: ' + combo.currentText
            }
        }
    }


}