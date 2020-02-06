import QtQuick 2.14
import QtQuick.Window 2.2
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.0

RowLayout{
    property bool tickState
    property bool displayBusy

    Layout.fillWidth: true

    //b

    BusyIndicator{
        visible: displayBusy
        running: true
    }
    Image {

        visible: !displayBusy && !tickState
        id: pasok
        source: "qrc:/Images/mauvaiseinfo.svg"
        sourceSize.width: 50
    }
    Image {

        visible: !displayBusy && tickState
        id: ok
        source: "qrc:/Images/bonneinfo.svg"
        sourceSize.width: 50
    }
}
