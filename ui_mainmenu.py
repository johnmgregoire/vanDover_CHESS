# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JohnnyG\Documents\CHESS\XRDproject_Python\mainmenu.ui'
#
# Created: Sun Oct 30 22:45:28 2011
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1025, 412)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/CUicon.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        self.bodywidget = QtGui.QWidget(MainMenu)
        self.bodywidget.setObjectName("bodywidget")
        self.tasklistLabel = QtGui.QLabel(self.bodywidget)
        self.tasklistLabel.setGeometry(QtCore.QRect(9, 10, 1006, 16))
        self.tasklistLabel.setObjectName("tasklistLabel")
        self.taskTextBrowser = QtGui.QTextBrowser(self.bodywidget)
        self.taskTextBrowser.setGeometry(QtCore.QRect(10, 28, 1006, 231))
        self.taskTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.taskTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.taskTextBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.taskTextBrowser.setReadOnly(False)
        self.taskTextBrowser.setObjectName("taskTextBrowser")
        self.performPushButton = QtGui.QPushButton(self.bodywidget)
        self.performPushButton.setGeometry(QtCore.QRect(9, 264, 1006, 23))
        self.performPushButton.setStyleSheet("""background-color: lightblue
""")
        self.performPushButton.setObjectName("performPushButton")
        self.active_file_lineEdit = QtGui.QLineEdit(self.bodywidget)
        self.active_file_lineEdit.setGeometry(QtCore.QRect(9, 293, 1006, 20))
        self.active_file_lineEdit.setObjectName("active_file_lineEdit")
        self.activepathcheckBox = QtGui.QCheckBox(self.bodywidget)
        self.activepathcheckBox.setGeometry(QtCore.QRect(9, 319, 166, 18))
        self.activepathcheckBox.setChecked(True)
        self.activepathcheckBox.setObjectName("activepathcheckBox")
        self.default_scan_checkBox = QtGui.QCheckBox(self.bodywidget)
        self.default_scan_checkBox.setGeometry(QtCore.QRect(190, 320, 241, 18))
        self.default_scan_checkBox.setChecked(True)
        self.default_scan_checkBox.setObjectName("default_scan_checkBox")
        self.navchoiceComboBox = QtGui.QComboBox(self.bodywidget)
        self.navchoiceComboBox.setGeometry(QtCore.QRect(725, 320, 121, 24))
        self.navchoiceComboBox.setObjectName("navchoiceComboBox")
        self.navchoiceComboBox.addItem(QtCore.QString())
        self.navchoiceComboBox.addItem(QtCore.QString())
        self.navchoiceComboBox.addItem(QtCore.QString())
        self.label = QtGui.QLabel(self.bodywidget)
        self.label.setGeometry(QtCore.QRect(580, 320, 136, 20))
        self.label.setObjectName("label")
        MainMenu.setCentralWidget(self.bodywidget)
        self.main_menu_pulldown = QtGui.QMenuBar(MainMenu)
        self.main_menu_pulldown.setGeometry(QtCore.QRect(0, 0, 1025, 23))
        self.main_menu_pulldown.setObjectName("main_menu_pulldown")
        self.menuXRD_analysis_for_MAR345 = QtGui.QMenu(self.main_menu_pulldown)
        self.menuXRD_analysis_for_MAR345.setObjectName("menuXRD_analysis_for_MAR345")
        self.menuData_Analysis = QtGui.QMenu(self.main_menu_pulldown)
        self.menuData_Analysis.setObjectName("menuData_Analysis")
        self.menuPerform_integration = QtGui.QMenu(self.menuData_Analysis)
        self.menuPerform_integration.setObjectName("menuPerform_integration")
        self.menu1d_peak_search = QtGui.QMenu(self.menuData_Analysis)
        self.menu1d_peak_search.setObjectName("menu1d_peak_search")
        self.menuVisualization = QtGui.QMenu(self.main_menu_pulldown)
        self.menuVisualization.setObjectName("menuVisualization")
        self.menuExit = QtGui.QMenu(self.main_menu_pulldown)
        self.menuExit.setObjectName("menuExit")
        self.menuData_Export = QtGui.QMenu(self.main_menu_pulldown)
        self.menuData_Export.setObjectName("menuData_Export")
        self.menuCHESSrun = QtGui.QMenu(self.main_menu_pulldown)
        self.menuCHESSrun.setObjectName("menuCHESSrun")
        self.menuWavelets = QtGui.QMenu(self.main_menu_pulldown)
        self.menuWavelets.setObjectName("menuWavelets")
        self.menuComposition = QtGui.QMenu(self.main_menu_pulldown)
        self.menuComposition.setObjectName("menuComposition")
        self.menuMiniPrograms = QtGui.QMenu(self.main_menu_pulldown)
        self.menuMiniPrograms.setObjectName("menuMiniPrograms")
        self.menuTexture_analysis = QtGui.QMenu(self.main_menu_pulldown)
        self.menuTexture_analysis.setObjectName("menuTexture_analysis")
        self.menuInDevelopment = QtGui.QMenu(self.main_menu_pulldown)
        self.menuInDevelopment.setObjectName("menuInDevelopment")
        self.menuAssociate_1d_peaks_with_qqpeaks_2 = QtGui.QMenu(self.menuInDevelopment)
        self.menuAssociate_1d_peaks_with_qqpeaks_2.setObjectName("menuAssociate_1d_peaks_with_qqpeaks_2")
        MainMenu.setMenuBar(self.main_menu_pulldown)
        self.statusbar = QtGui.QStatusBar(MainMenu)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)
        self.action_import_single_image = QtGui.QAction(MainMenu)
        self.action_import_single_image.setObjectName("action_import_single_image")
        self.action_import_entire_dataset = QtGui.QAction(MainMenu)
        self.action_import_entire_dataset.setObjectName("action_import_entire_dataset")
        self.action_edit_DAQ_params = QtGui.QAction(MainMenu)
        self.action_edit_DAQ_params.setObjectName("action_edit_DAQ_params")
        self.action_choose_background = QtGui.QAction(MainMenu)
        self.action_choose_background.setObjectName("action_choose_background")
        self.action_choose_data_subset = QtGui.QAction(MainMenu)
        self.action_choose_data_subset.setObjectName("action_choose_data_subset")
        self.action_choose_excluded_pixels = QtGui.QAction(MainMenu)
        self.action_choose_excluded_pixels.setObjectName("action_choose_excluded_pixels")
        self.action_build_integration_map = QtGui.QAction(MainMenu)
        self.action_build_integration_map.setObjectName("action_build_integration_map")
        self.action_integrate_single_image = QtGui.QAction(MainMenu)
        self.action_integrate_single_image.setObjectName("action_integrate_single_image")
        self.action_integrate_entire_dataset = QtGui.QAction(MainMenu)
        self.action_integrate_entire_dataset.setObjectName("action_integrate_entire_dataset")
        self.action_qq_single_image = QtGui.QAction(MainMenu)
        self.action_qq_single_image.setObjectName("action_qq_single_image")
        self.action_qq_entire_dataset = QtGui.QAction(MainMenu)
        self.action_qq_entire_dataset.setObjectName("action_qq_entire_dataset")
        self.action_analyze_qq = QtGui.QAction(MainMenu)
        self.action_analyze_qq.setObjectName("action_analyze_qq")
        self.action_plot_2D_intensity = QtGui.QAction(MainMenu)
        self.action_plot_2D_intensity.setObjectName("action_plot_2D_intensity")
        self.action_plot_1D_intensity = QtGui.QAction(MainMenu)
        self.action_plot_1D_intensity.setObjectName("action_plot_1D_intensity")
        self.action_plot_1D_texture = QtGui.QAction(MainMenu)
        self.action_plot_1D_texture.setObjectName("action_plot_1D_texture")
        self.action_plot_qq = QtGui.QAction(MainMenu)
        self.action_plot_qq.setObjectName("action_plot_qq")
        self.actionExit = QtGui.QAction(MainMenu)
        self.actionExit.setObjectName("actionExit")
        self.action_calc_background = QtGui.QAction(MainMenu)
        self.action_calc_background.setObjectName("action_calc_background")
        self.action_import_int_kill_map = QtGui.QAction(MainMenu)
        self.action_import_int_kill_map.setObjectName("action_import_int_kill_map")
        self.action_plot_imap = QtGui.QAction(MainMenu)
        self.action_plot_imap.setObjectName("action_plot_imap")
        self.action_save_all_1d_plt = QtGui.QAction(MainMenu)
        self.action_save_all_1d_plt.setObjectName("action_save_all_1d_plt")
        self.action_calc_bcknd = QtGui.QAction(MainMenu)
        self.action_calc_bcknd.setObjectName("action_calc_bcknd")
        self.action_plot_dat = QtGui.QAction(MainMenu)
        self.action_plot_dat.setObjectName("action_plot_dat")
        self.action_image_histogram = QtGui.QAction(MainMenu)
        self.action_image_histogram.setObjectName("action_image_histogram")
        self.action_H5file_info = QtGui.QAction(MainMenu)
        self.action_H5file_info.setObjectName("action_H5file_info")
        self.action_process_1d = QtGui.QAction(MainMenu)
        self.action_process_1d.setObjectName("action_process_1d")
        self.action_group_into_phases = QtGui.QAction(MainMenu)
        self.action_group_into_phases.setObjectName("action_group_into_phases")
        self.action_1d_peak_search_single = QtGui.QAction(MainMenu)
        self.action_1d_peak_search_single.setObjectName("action_1d_peak_search_single")
        self.action_1d_peak_search_all = QtGui.QAction(MainMenu)
        self.action_1d_peak_search_all.setObjectName("action_1d_peak_search_all")
        self.action_associate_1d_qqpeaks_single = QtGui.QAction(MainMenu)
        self.action_associate_1d_qqpeaks_single.setObjectName("action_associate_1d_qqpeaks_single")
        self.action_associate_1d_qqpeaks_all = QtGui.QAction(MainMenu)
        self.action_associate_1d_qqpeaks_all.setObjectName("action_associate_1d_qqpeaks_all")
        self.action_association_trees = QtGui.QAction(MainMenu)
        self.action_association_trees.setObjectName("action_association_trees")
        self.action_save_2d_image_dataset = QtGui.QAction(MainMenu)
        self.action_save_2d_image_dataset.setObjectName("action_save_2d_image_dataset")
        self.action_build_chi_map = QtGui.QAction(MainMenu)
        self.action_build_chi_map.setObjectName("action_build_chi_map")
        self.action_spatial_phases = QtGui.QAction(MainMenu)
        self.action_spatial_phases.setObjectName("action_spatial_phases")
        self.actionBinImapChimap = QtGui.QAction(MainMenu)
        self.actionBinImapChimap.setObjectName("actionBinImapChimap")
        self.action_import_sample_info = QtGui.QAction(MainMenu)
        self.action_import_sample_info.setObjectName("action_import_sample_info")
        self.action_export_XRDSuite_files = QtGui.QAction(MainMenu)
        self.action_export_XRDSuite_files.setObjectName("action_export_XRDSuite_files")
        self.action_initialize_scan = QtGui.QAction(MainMenu)
        self.action_initialize_scan.setObjectName("action_initialize_scan")
        self.action_change_active_scan = QtGui.QAction(MainMenu)
        self.action_change_active_scan.setObjectName("action_change_active_scan")
        self.action_createchessrun = QtGui.QAction(MainMenu)
        self.action_createchessrun.setObjectName("action_createchessrun")
        self.action_calcqchiimages = QtGui.QAction(MainMenu)
        self.action_calcqchiimages.setObjectName("action_calcqchiimages")
        self.action_calcqq = QtGui.QAction(MainMenu)
        self.action_calcqq.setObjectName("action_calcqq")
        self.action_calc_waveset1d = QtGui.QAction(MainMenu)
        self.action_calc_waveset1d.setObjectName("action_calc_waveset1d")
        self.action_wavetrans1d = QtGui.QAction(MainMenu)
        self.action_wavetrans1d.setObjectName("action_wavetrans1d")
        self.action_plot1dwavetrans = QtGui.QAction(MainMenu)
        self.action_plot1dwavetrans.setObjectName("action_plot1dwavetrans")
        self.action_fit_1d_peaks = QtGui.QAction(MainMenu)
        self.action_fit_1d_peaks.setObjectName("action_fit_1d_peaks")
        self.action_fix1dbcknd = QtGui.QAction(MainMenu)
        self.action_fix1dbcknd.setObjectName("action_fix1dbcknd")
        self.action_addpeaks = QtGui.QAction(MainMenu)
        self.action_addpeaks.setObjectName("action_addpeaks")
        self.action_plotinterpimageof1ddata = QtGui.QAction(MainMenu)
        self.action_plotinterpimageof1ddata.setObjectName("action_plotinterpimageof1ddata")
        self.action_removepeaks = QtGui.QAction(MainMenu)
        self.action_removepeaks.setObjectName("action_removepeaks")
        self.actionDeposition_Profiling = QtGui.QAction(MainMenu)
        self.actionDeposition_Profiling.setObjectName("actionDeposition_Profiling")
        self.actionXRF_analysis = QtGui.QAction(MainMenu)
        self.actionXRF_analysis.setObjectName("actionXRF_analysis")
        self.action_plot_sample_info = QtGui.QAction(MainMenu)
        self.action_plot_sample_info.setObjectName("action_plot_sample_info")
        self.action_synthimport = QtGui.QAction(MainMenu)
        self.action_synthimport.setObjectName("action_synthimport")
        self.action_exportpeak = QtGui.QAction(MainMenu)
        self.action_exportpeak.setObjectName("action_exportpeak")
        self.action_neighbor_calculation = QtGui.QAction(MainMenu)
        self.action_neighbor_calculation.setObjectName("action_neighbor_calculation")
        self.action_plot_chessrun_arrays = QtGui.QAction(MainMenu)
        self.action_plot_chessrun_arrays.setObjectName("action_plot_chessrun_arrays")
        self.action_buildnewscan = QtGui.QAction(MainMenu)
        self.action_buildnewscan.setObjectName("action_buildnewscan")
        self.action_mini_program_txt = QtGui.QAction(MainMenu)
        self.action_mini_program_txt.setObjectName("action_mini_program_txt")
        self.action_import_txt_XRD_data = QtGui.QAction(MainMenu)
        self.action_import_txt_XRD_data.setObjectName("action_import_txt_XRD_data")
        self.action_export_cfg = QtGui.QAction(MainMenu)
        self.action_export_cfg.setObjectName("action_export_cfg")
        self.action_textureanalysis = QtGui.QAction(MainMenu)
        self.action_textureanalysis.setObjectName("action_textureanalysis")
        self.action_wavetranstex = QtGui.QAction(MainMenu)
        self.action_wavetranstex.setObjectName("action_wavetranstex")
        self.action_1d_peak_search_tex = QtGui.QAction(MainMenu)
        self.action_1d_peak_search_tex.setObjectName("action_1d_peak_search_tex")
        self.action_process_texture = QtGui.QAction(MainMenu)
        self.action_process_texture.setObjectName("action_process_texture")
        self.action_fit_1d_peaks_tex = QtGui.QAction(MainMenu)
        self.action_fit_1d_peaks_tex.setObjectName("action_fit_1d_peaks_tex")
        self.action_bckndinventory = QtGui.QAction(MainMenu)
        self.action_bckndinventory.setObjectName("action_bckndinventory")
        self.action_edit_raw_diff_data = QtGui.QAction(MainMenu)
        self.action_edit_raw_diff_data.setObjectName("action_edit_raw_diff_data")
        self.action_copy_lin_bcknd = QtGui.QAction(MainMenu)
        self.action_copy_lin_bcknd.setObjectName("action_copy_lin_bcknd")
        self.actionLinBcknd1d = QtGui.QAction(MainMenu)
        self.actionLinBcknd1d.setObjectName("actionLinBcknd1d")
        self.action_batch_initialize = QtGui.QAction(MainMenu)
        self.action_batch_initialize.setObjectName("action_batch_initialize")
        self.menuXRD_analysis_for_MAR345.addAction(self.action_initialize_scan)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_edit_DAQ_params)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_change_active_scan)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_buildnewscan)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_import_int_kill_map)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_import_sample_info)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_synthimport)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_import_txt_XRD_data)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_copy_lin_bcknd)
        self.menuXRD_analysis_for_MAR345.addAction(self.action_batch_initialize)
        self.menuPerform_integration.addAction(self.action_integrate_single_image)
        self.menuPerform_integration.addAction(self.action_integrate_entire_dataset)
        self.menu1d_peak_search.addAction(self.action_1d_peak_search_single)
        self.menu1d_peak_search.addAction(self.action_1d_peak_search_all)
        self.menuData_Analysis.addAction(self.action_edit_raw_diff_data)
        self.menuData_Analysis.addAction(self.action_choose_data_subset)
        self.menuData_Analysis.addAction(self.action_calc_bcknd)
        self.menuData_Analysis.addAction(self.menuPerform_integration.menuAction())
        self.menuData_Analysis.addAction(self.actionLinBcknd1d)
        self.menuData_Analysis.addAction(self.action_process_1d)
        self.menuData_Analysis.addAction(self.action_wavetrans1d)
        self.menuData_Analysis.addAction(self.menu1d_peak_search.menuAction())
        self.menuData_Analysis.addAction(self.action_fit_1d_peaks)
        self.menuData_Analysis.addAction(self.action_addpeaks)
        self.menuData_Analysis.addAction(self.action_removepeaks)
        self.menuData_Analysis.addAction(self.action_fix1dbcknd)
        self.menuVisualization.addAction(self.action_plot_2D_intensity)
        self.menuVisualization.addAction(self.action_plot_1D_intensity)
        self.menuVisualization.addAction(self.action_plot1dwavetrans)
        self.menuVisualization.addAction(self.action_plot_1D_texture)
        self.menuVisualization.addAction(self.action_plotinterpimageof1ddata)
        self.menuVisualization.addAction(self.action_plot_sample_info)
        self.menuVisualization.addAction(self.action_plot_qq)
        self.menuVisualization.addAction(self.action_association_trees)
        self.menuVisualization.addAction(self.action_plot_imap)
        self.menuVisualization.addAction(self.action_plot_dat)
        self.menuVisualization.addAction(self.action_image_histogram)
        self.menuVisualization.addAction(self.action_H5file_info)
        self.menuExit.addAction(self.actionExit)
        self.menuData_Export.addAction(self.action_save_all_1d_plt)
        self.menuData_Export.addAction(self.action_save_2d_image_dataset)
        self.menuData_Export.addAction(self.action_export_XRDSuite_files)
        self.menuData_Export.addAction(self.action_exportpeak)
        self.menuCHESSrun.addAction(self.action_createchessrun)
        self.menuCHESSrun.addAction(self.action_calcqchiimages)
        self.menuCHESSrun.addAction(self.action_build_integration_map)
        self.menuCHESSrun.addAction(self.action_build_chi_map)
        self.menuCHESSrun.addAction(self.actionBinImapChimap)
        self.menuCHESSrun.addSeparator()
        self.menuCHESSrun.addAction(self.action_plot_chessrun_arrays)
        self.menuCHESSrun.addAction(self.action_bckndinventory)
        self.menuWavelets.addAction(self.action_calc_waveset1d)
        self.menuComposition.addAction(self.actionDeposition_Profiling)
        self.menuComposition.addAction(self.actionXRF_analysis)
        self.menuComposition.addAction(self.action_export_cfg)
        self.menuMiniPrograms.addAction(self.action_mini_program_txt)
        self.menuTexture_analysis.addAction(self.action_textureanalysis)
        self.menuTexture_analysis.addAction(self.action_wavetranstex)
        self.menuTexture_analysis.addAction(self.action_1d_peak_search_tex)
        self.menuTexture_analysis.addAction(self.action_process_texture)
        self.menuTexture_analysis.addAction(self.action_fit_1d_peaks_tex)
        self.menuAssociate_1d_peaks_with_qqpeaks_2.addAction(self.action_associate_1d_qqpeaks_single)
        self.menuAssociate_1d_peaks_with_qqpeaks_2.addAction(self.action_associate_1d_qqpeaks_all)
        self.menuInDevelopment.addAction(self.action_calcqq)
        self.menuInDevelopment.addAction(self.action_analyze_qq)
        self.menuInDevelopment.addAction(self.action_group_into_phases)
        self.menuInDevelopment.addAction(self.action_spatial_phases)
        self.menuInDevelopment.addAction(self.action_neighbor_calculation)
        self.menuInDevelopment.addAction(self.menuAssociate_1d_peaks_with_qqpeaks_2.menuAction())
        self.main_menu_pulldown.addAction(self.menuXRD_analysis_for_MAR345.menuAction())
        self.main_menu_pulldown.addAction(self.menuData_Analysis.menuAction())
        self.main_menu_pulldown.addAction(self.menuTexture_analysis.menuAction())
        self.main_menu_pulldown.addAction(self.menuComposition.menuAction())
        self.main_menu_pulldown.addAction(self.menuVisualization.menuAction())
        self.main_menu_pulldown.addAction(self.menuData_Export.menuAction())
        self.main_menu_pulldown.addAction(self.menuCHESSrun.menuAction())
        self.main_menu_pulldown.addAction(self.menuWavelets.menuAction())
        self.main_menu_pulldown.addAction(self.menuMiniPrograms.menuAction())
        self.main_menu_pulldown.addAction(self.menuInDevelopment.menuAction())
        self.main_menu_pulldown.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QtGui.QApplication.translate("MainMenu", "XRD analysis for mar345: tools for composition spread phase mapping", None, QtGui.QApplication.UnicodeUTF8))
        self.tasklistLabel.setText(QtGui.QApplication.translate("MainMenu", "tasks to be performed", None, QtGui.QApplication.UnicodeUTF8))
        self.taskTextBrowser.setToolTip(QtGui.QApplication.translate("MainMenu", "This is a list of commands for data analysis. The commands can be entered manually but will be entered for you through the selection of the above menu items. In the execution of these tasks, ACTIVEPATH and ACTIVEGRP are string objects that will initially be the path and group associated with the below \"Active path enabled\" section, but these objects can be redefined as needed. The command ACTIVEGRP=DEFAULT will make ACTIVEGRP be the default spec group for the present ACTIVEPATH.", None, QtGui.QApplication.UnicodeUTF8))
        self.taskTextBrowser.setHtml(QtGui.QApplication.translate("MainMenu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.performPushButton.setToolTip(QtGui.QApplication.translate("MainMenu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When this is clicked, the commands in the above text editor will be performed. During these operations, this window will be inactive. You will be notified with a message box when the commands have been completed.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.performPushButton.setText(QtGui.QApplication.translate("MainMenu", "Perform Above Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.activepathcheckBox.setToolTip(QtGui.QApplication.translate("MainMenu", "If this is checked and the above field contains a valid .h5 and group name, then that group will aotumatically be used when a routine is activated through the above menus. If you wish to access data from a different experiment, uncheck this box.", None, QtGui.QApplication.UnicodeUTF8))
        self.activepathcheckBox.setText(QtGui.QApplication.translate("MainMenu", "Active path enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.default_scan_checkBox.setToolTip(QtGui.QApplication.translate("MainMenu", "If both this checkbox and \"Active path enabled\" are unchecked, then when a new .h5 is opened, you will have the choice of choosing a new spec measurement scan for analysis.", None, QtGui.QApplication.UnicodeUTF8))
        self.default_scan_checkBox.setText(QtGui.QApplication.translate("MainMenu", "use default measurement scan", None, QtGui.QApplication.UnicodeUTF8))
        self.navchoiceComboBox.setToolTip(QtGui.QApplication.translate("MainMenu", "This specifies the style fot he navigator for applications that have a clickable naviagtor for spec index selection. \"Posn\" style navigator has an outline of the substrate with measurement point indiciated by the spec x,z position. A \"Comp\" style navigator will be a ternary composition plot - these require that the composition data be available.", None, QtGui.QApplication.UnicodeUTF8))
        self.navchoiceComboBox.setItemText(0, QtGui.QApplication.translate("MainMenu", "x,z Posn", None, QtGui.QApplication.UnicodeUTF8))
        self.navchoiceComboBox.setItemText(1, QtGui.QApplication.translate("MainMenu", "DepProf comp.", None, QtGui.QApplication.UnicodeUTF8))
        self.navchoiceComboBox.setItemText(2, QtGui.QApplication.translate("MainMenu", "XRF comp.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainMenu", "Plot Navigator Style:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuXRD_analysis_for_MAR345.setTitle(QtGui.QApplication.translate("MainMenu", "Data &Import", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData_Analysis.setTitle(QtGui.QApplication.translate("MainMenu", "&Diffraction Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPerform_integration.setTitle(QtGui.QApplication.translate("MainMenu", "perform &integration", None, QtGui.QApplication.UnicodeUTF8))
        self.menu1d_peak_search.setTitle(QtGui.QApplication.translate("MainMenu", "1D wavelet peak search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVisualization.setTitle(QtGui.QApplication.translate("MainMenu", "&Visualization", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExit.setTitle(QtGui.QApplication.translate("MainMenu", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData_Export.setTitle(QtGui.QApplication.translate("MainMenu", "Data Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCHESSrun.setTitle(QtGui.QApplication.translate("MainMenu", "CHESSrun Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWavelets.setTitle(QtGui.QApplication.translate("MainMenu", "Wavelets Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.menuComposition.setTitle(QtGui.QApplication.translate("MainMenu", "&Composition", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMiniPrograms.setTitle(QtGui.QApplication.translate("MainMenu", "Batch Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTexture_analysis.setTitle(QtGui.QApplication.translate("MainMenu", "&Texture Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInDevelopment.setTitle(QtGui.QApplication.translate("MainMenu", "InDevelopment", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAssociate_1d_peaks_with_qqpeaks_2.setTitle(QtGui.QApplication.translate("MainMenu", "associate 1d peaks with qqpeaks", None, QtGui.QApplication.UnicodeUTF8))
        self.action_import_single_image.setText(QtGui.QApplication.translate("MainMenu", "&single image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_import_entire_dataset.setText(QtGui.QApplication.translate("MainMenu", "&entire dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.action_edit_DAQ_params.setText(QtGui.QApplication.translate("MainMenu", "&edit DAQ parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.action_choose_background.setText(QtGui.QApplication.translate("MainMenu", "choose &background", None, QtGui.QApplication.UnicodeUTF8))
        self.action_choose_data_subset.setText(QtGui.QApplication.translate("MainMenu", "&edit point list for analysis and killmap", None, QtGui.QApplication.UnicodeUTF8))
        self.action_choose_excluded_pixels.setText(QtGui.QApplication.translate("MainMenu", "choose &excluded pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.action_build_integration_map.setText(QtGui.QApplication.translate("MainMenu", "build integration &map", None, QtGui.QApplication.UnicodeUTF8))
        self.action_integrate_single_image.setText(QtGui.QApplication.translate("MainMenu", "&single image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_integrate_entire_dataset.setText(QtGui.QApplication.translate("MainMenu", "&entire dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.action_qq_single_image.setText(QtGui.QApplication.translate("MainMenu", "&single image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_qq_entire_dataset.setText(QtGui.QApplication.translate("MainMenu", "&entire dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.action_analyze_qq.setText(QtGui.QApplication.translate("MainMenu", "&analyze QQ (find peaks, qqnorm)", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_2D_intensity.setText(QtGui.QApplication.translate("MainMenu", "plot &2D intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_1D_intensity.setText(QtGui.QApplication.translate("MainMenu", "plot &1D intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_1D_texture.setText(QtGui.QApplication.translate("MainMenu", "plot 1D &texture", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_qq.setText(QtGui.QApplication.translate("MainMenu", "plot qq", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainMenu", "exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_calc_background.setText(QtGui.QApplication.translate("MainMenu", "(re)calculate &background", None, QtGui.QApplication.UnicodeUTF8))
        self.action_import_int_kill_map.setText(QtGui.QApplication.translate("MainMenu", "import integration map, etc. from library", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_imap.setText(QtGui.QApplication.translate("MainMenu", "plot &integration map", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_all_1d_plt.setText(QtGui.QApplication.translate("MainMenu", "save all &1d Int as .plt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_calc_bcknd.setText(QtGui.QApplication.translate("MainMenu", "(re)calculate &background", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_dat.setText(QtGui.QApplication.translate("MainMenu", "plot .dat binary images", None, QtGui.QApplication.UnicodeUTF8))
        self.action_image_histogram.setText(QtGui.QApplication.translate("MainMenu", "image histogram", None, QtGui.QApplication.UnicodeUTF8))
        self.action_H5file_info.setText(QtGui.QApplication.translate("MainMenu", "h5file info", None, QtGui.QApplication.UnicodeUTF8))
        self.action_process_1d.setText(QtGui.QApplication.translate("MainMenu", "process 1D intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.action_group_into_phases.setText(QtGui.QApplication.translate("MainMenu", "group 1d peaks", None, QtGui.QApplication.UnicodeUTF8))
        self.action_1d_peak_search_single.setText(QtGui.QApplication.translate("MainMenu", "single image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_1d_peak_search_all.setText(QtGui.QApplication.translate("MainMenu", "entire dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.action_associate_1d_qqpeaks_single.setText(QtGui.QApplication.translate("MainMenu", "single image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_associate_1d_qqpeaks_all.setText(QtGui.QApplication.translate("MainMenu", "entire dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.action_association_trees.setText(QtGui.QApplication.translate("MainMenu", "qqpeak-ipeak association", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_2d_image_dataset.setText(QtGui.QApplication.translate("MainMenu", "save 2d image dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.action_build_chi_map.setText(QtGui.QApplication.translate("MainMenu", "build chi map", None, QtGui.QApplication.UnicodeUTF8))
        self.action_spatial_phases.setText(QtGui.QApplication.translate("MainMenu", "spatial analysis of phases", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBinImapChimap.setText(QtGui.QApplication.translate("MainMenu", "bin imap, chimap, killmap", None, QtGui.QApplication.UnicodeUTF8))
        self.action_import_sample_info.setText(QtGui.QApplication.translate("MainMenu", "import \"other\" sample data (.txt with spec indeces)", None, QtGui.QApplication.UnicodeUTF8))
        self.action_export_XRDSuite_files.setText(QtGui.QApplication.translate("MainMenu", "export XRDSuite files", None, QtGui.QApplication.UnicodeUTF8))
        self.action_initialize_scan.setText(QtGui.QApplication.translate("MainMenu", "initialize measurement scan", None, QtGui.QApplication.UnicodeUTF8))
        self.action_change_active_scan.setText(QtGui.QApplication.translate("MainMenu", "change active analysis scan#", None, QtGui.QApplication.UnicodeUTF8))
        self.action_createchessrun.setText(QtGui.QApplication.translate("MainMenu", "Create CHESSrun group", None, QtGui.QApplication.UnicodeUTF8))
        self.action_calcqchiimages.setText(QtGui.QApplication.translate("MainMenu", "calculate q,chi,dqchi images", None, QtGui.QApplication.UnicodeUTF8))
        self.action_calcqq.setText(QtGui.QApplication.translate("MainMenu", "calc QQ", None, QtGui.QApplication.UnicodeUTF8))
        self.action_calc_waveset1d.setText(QtGui.QApplication.translate("MainMenu", "calc 1d wavelet set", None, QtGui.QApplication.UnicodeUTF8))
        self.action_wavetrans1d.setText(QtGui.QApplication.translate("MainMenu", "wavelet transform 1d data", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot1dwavetrans.setText(QtGui.QApplication.translate("MainMenu", "plot 1D wavetrans", None, QtGui.QApplication.UnicodeUTF8))
        self.action_fit_1d_peaks.setText(QtGui.QApplication.translate("MainMenu", "fit 1D peaks", None, QtGui.QApplication.UnicodeUTF8))
        self.action_fix1dbcknd.setText(QtGui.QApplication.translate("MainMenu", "edit 1D bcknd using existing peaks", None, QtGui.QApplication.UnicodeUTF8))
        self.action_addpeaks.setText(QtGui.QApplication.translate("MainMenu", "add peaks to peak-fit-list", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plotinterpimageof1ddata.setText(QtGui.QApplication.translate("MainMenu", "interp 2dimage. diffraction vs info", None, QtGui.QApplication.UnicodeUTF8))
        self.action_removepeaks.setText(QtGui.QApplication.translate("MainMenu", "remove peaks from post-fitted list", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeposition_Profiling.setText(QtGui.QApplication.translate("MainMenu", "Deposition Profiling", None, QtGui.QApplication.UnicodeUTF8))
        self.actionXRF_analysis.setText(QtGui.QApplication.translate("MainMenu", "XRF analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_sample_info.setText(QtGui.QApplication.translate("MainMenu", "plot sample info / metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.action_synthimport.setText(QtGui.QApplication.translate("MainMenu", "import synthetic XRD data (.txt with peaks)", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exportpeak.setText(QtGui.QApplication.translate("MainMenu", "export peak list", None, QtGui.QApplication.UnicodeUTF8))
        self.action_neighbor_calculation.setText(QtGui.QApplication.translate("MainMenu", "neighboring points calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.action_plot_chessrun_arrays.setText(QtGui.QApplication.translate("MainMenu", "plot arrays", None, QtGui.QApplication.UnicodeUTF8))
        self.action_buildnewscan.setText(QtGui.QApplication.translate("MainMenu", "compile new measurement scan", None, QtGui.QApplication.UnicodeUTF8))
        self.action_mini_program_txt.setText(QtGui.QApplication.translate("MainMenu", "load from txt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_import_txt_XRD_data.setText(QtGui.QApplication.translate("MainMenu", "import txt XRD data", None, QtGui.QApplication.UnicodeUTF8))
        self.action_export_cfg.setText(QtGui.QApplication.translate("MainMenu", "Export pymca cfg as .cfg", None, QtGui.QApplication.UnicodeUTF8))
        self.action_textureanalysis.setText(QtGui.QApplication.translate("MainMenu", "get PHI-distribution of peak", None, QtGui.QApplication.UnicodeUTF8))
        self.action_wavetranstex.setText(QtGui.QApplication.translate("MainMenu", "wavelet tranform PHI-dist", None, QtGui.QApplication.UnicodeUTF8))
        self.action_1d_peak_search_tex.setText(QtGui.QApplication.translate("MainMenu", "wavelet peak search PHI-dist", None, QtGui.QApplication.UnicodeUTF8))
        self.action_process_texture.setText(QtGui.QApplication.translate("MainMenu", "process PHI-dist", None, QtGui.QApplication.UnicodeUTF8))
        self.action_fit_1d_peaks_tex.setText(QtGui.QApplication.translate("MainMenu", "fit peaks", None, QtGui.QApplication.UnicodeUTF8))
        self.action_bckndinventory.setText(QtGui.QApplication.translate("MainMenu", "inventory a bcknd image from sample .h5", None, QtGui.QApplication.UnicodeUTF8))
        self.action_edit_raw_diff_data.setText(QtGui.QApplication.translate("MainMenu", "edit raw diffraction data", None, QtGui.QApplication.UnicodeUTF8))
        self.action_copy_lin_bcknd.setText(QtGui.QApplication.translate("MainMenu", "copy \"linear bcknd\" source data from other .h5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLinBcknd1d.setText(QtGui.QApplication.translate("MainMenu", "Linear Bcknd process 1d data", None, QtGui.QApplication.UnicodeUTF8))
        self.action_batch_initialize.setText(QtGui.QApplication.translate("MainMenu", "batch initialize scans in same .h5", None, QtGui.QApplication.UnicodeUTF8))

