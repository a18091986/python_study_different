import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:600
    height:400
    title:'scrollview'


    ScrollView{

            width:200
            height:200


            Label
            {
            text:'Python'
            font.pixelSize:100
            }
        }

}