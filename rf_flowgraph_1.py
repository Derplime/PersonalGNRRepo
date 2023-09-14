#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Loopback Test 1
# Author: derplime
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time



class rf_flowgraph_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Loopback Test 1", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Loopback Test 1")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rf_flowgraph_1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.uhd_sample_rate = uhd_sample_rate = 500000
        self.uhd_gain = uhd_gain = 1
        self.uhd_center_freq = uhd_center_freq = 100000000
        self.uhd_bw = uhd_bw = 1000000
        self.signal_src_samp_rate = signal_src_samp_rate = 1000000
        self.signal_src_freq = signal_src_freq = 10000

        ##################################################
        # Blocks
        ##################################################

        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("addr=192.168.10.2", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(uhd_sample_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0.set_center_freq(uhd_center_freq, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_bandwidth(uhd_bw, 0)
        self.uhd_usrp_source_0.set_gain(uhd_gain, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("addr=192.168.10.2", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate(uhd_sample_rate)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_sink_0.set_center_freq(uhd_center_freq, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_bandwidth(uhd_bw, 0)
        self.uhd_usrp_sink_0.set_gain(uhd_gain, 0)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'rf_flowgraph_1.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_c(signal_src_samp_rate, analog.GR_COS_WAVE, signal_src_freq, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rf_flowgraph_1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_uhd_sample_rate(self):
        return self.uhd_sample_rate

    def set_uhd_sample_rate(self, uhd_sample_rate):
        self.uhd_sample_rate = uhd_sample_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.uhd_sample_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.uhd_sample_rate)

    def get_uhd_gain(self):
        return self.uhd_gain

    def set_uhd_gain(self, uhd_gain):
        self.uhd_gain = uhd_gain
        self.uhd_usrp_sink_0.set_gain(self.uhd_gain, 0)
        self.uhd_usrp_source_0.set_gain(self.uhd_gain, 0)

    def get_uhd_center_freq(self):
        return self.uhd_center_freq

    def set_uhd_center_freq(self, uhd_center_freq):
        self.uhd_center_freq = uhd_center_freq
        self.uhd_usrp_sink_0.set_center_freq(self.uhd_center_freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.uhd_center_freq, 0)

    def get_uhd_bw(self):
        return self.uhd_bw

    def set_uhd_bw(self, uhd_bw):
        self.uhd_bw = uhd_bw
        self.uhd_usrp_sink_0.set_bandwidth(self.uhd_bw, 0)
        self.uhd_usrp_source_0.set_bandwidth(self.uhd_bw, 0)

    def get_signal_src_samp_rate(self):
        return self.signal_src_samp_rate

    def set_signal_src_samp_rate(self, signal_src_samp_rate):
        self.signal_src_samp_rate = signal_src_samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.signal_src_samp_rate)

    def get_signal_src_freq(self):
        return self.signal_src_freq

    def set_signal_src_freq(self, signal_src_freq):
        self.signal_src_freq = signal_src_freq
        self.analog_sig_source_x_0.set_frequency(self.signal_src_freq)




def main(top_block_cls=rf_flowgraph_1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
