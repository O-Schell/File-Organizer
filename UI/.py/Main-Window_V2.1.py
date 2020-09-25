/********************************************************************************
** Form generated from reading UI file 'Main-Window_V2.ui'
**
** Created by: Qt User Interface Compiler version 5.13.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAIN_2D_WINDOW_V2_H
#define UI_MAIN_2D_WINDOW_V2_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FileOrganizer
{
public:
    QWidget *centralwidget;
    QLabel *Title;
    QPushButton *Selectyourfolderbutton;
    QProgressBar *progressBar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *FileOrganizer)
    {
        if (FileOrganizer->objectName().isEmpty())
            FileOrganizer->setObjectName(QString::fromUtf8("FileOrganizer"));
        FileOrganizer->resize(800, 207);
        FileOrganizer->setAcceptDrops(false);
        FileOrganizer->setLayoutDirection(Qt::LeftToRight);
        FileOrganizer->setAnimated(true);
        FileOrganizer->setDockNestingEnabled(false);
        FileOrganizer->setUnifiedTitleAndToolBarOnMac(false);
        centralwidget = new QWidget(FileOrganizer);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        Title = new QLabel(centralwidget);
        Title->setObjectName(QString::fromUtf8("Title"));
        Title->setGeometry(QRect(200, 0, 450, 60));
        QFont font;
        font.setFamily(QString::fromUtf8("Panton Light Caps"));
        font.setPointSize(20);
        Title->setFont(font);
        Title->setAlignment(Qt::AlignCenter);
        Selectyourfolderbutton = new QPushButton(centralwidget);
        Selectyourfolderbutton->setObjectName(QString::fromUtf8("Selectyourfolderbutton"));
        Selectyourfolderbutton->setGeometry(QRect(320, 80, 160, 40));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Yu Gothic UI"));
        font1.setPointSize(12);
        Selectyourfolderbutton->setFont(font1);
        Selectyourfolderbutton->setAutoDefault(true);
        Selectyourfolderbutton->setFlat(false);
        progressBar = new QProgressBar(centralwidget);
        progressBar->setObjectName(QString::fromUtf8("progressBar"));
        progressBar->setGeometry(QRect(50, 150, 700, 20));
        progressBar->setValue(24);
        FileOrganizer->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(FileOrganizer);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        FileOrganizer->setStatusBar(statusbar);

        retranslateUi(FileOrganizer);

        Selectyourfolderbutton->setDefault(true);


        QMetaObject::connectSlotsByName(FileOrganizer);
    } // setupUi

    void retranslateUi(QMainWindow *FileOrganizer)
    {
        FileOrganizer->setWindowTitle(QCoreApplication::translate("FileOrganizer", "File-Organizer", nullptr));
        Title->setText(QCoreApplication::translate("FileOrganizer", "Welcome into File-Organizer !", nullptr));
        Selectyourfolderbutton->setText(QCoreApplication::translate("FileOrganizer", "Select your folder", nullptr));
    } // retranslateUi

};

namespace Ui {
    class FileOrganizer: public Ui_FileOrganizer {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAIN_2D_WINDOW_V2_H
