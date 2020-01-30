import QtQuick 2.6
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14

import "Attaque"
import "Defense"

ApplicationWindow {
    visible: true
    minimumWidth : mainLayout.implicitWidth
    minimumHeight : mainLayout.implicitHeight

    RowLayout{
        id : mainLayout
        Layout.margins : 20
        anchors.fill : parent
        spacing : 10
        RowLayout{}
        CarteAttaque{
            id : attaq
        }
        RowLayout{}

        ToolSeparator {
            Layout.fillHeight : true
            Layout.maximumHeight : attaq.implicitHeight + 40
        }
        RowLayout{}

        CarteDefense{

        }

        RowLayout{}
        focus : true                        
        Keys.onPressed: {
            if (event.key == Qt.Key_1 || event.key == 38) {
                stacklayout.currentIndex = 0
                event.accepted = true;
            }
            else if (event.key == Qt.Key_2 || event.key == 201) {
                stacklayout.currentIndex = 1
                event.accepted = true;
            }
            else if (event.key == Qt.Key_3 || event.key == 34) {
                stacklayout.currentIndex = 2
                event.accepted = true;
            }
            console.log(stacklayout.currentIndex)
        }
    }
            
}