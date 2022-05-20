from migen import *
from dma import *

class Math(Module):
    def __init__(self):
        self.dma_1 = dma_1 = Signal(32)
        self.dma_2 = dma_2 = Signal(32)
        self.alpha = alpha = 128

        self.res_1 = res_1 = Signal(32)
        self.res_2 = res_2 = Signal(32)
        self.res_3 = res_3 = Signal(32)
        self.res_4 = res_4 = Signal(32)
        self.res_5 = res_5 = Signal(32)

        self.sync += res_1.eq(alpha * dma_1)
        self.sync += res_2.eq(256 - alpha)
        self.sync += res_3.eq(res_2 * dma_2)
        self.sync += res_4.eq(res_1 + res_3)
        self.sync += res_5.eq(res_4 >> 8)

def pixel_processing(dut):
    for x in range(200):
        for y in range(100):
            for i in range(4):
                yield dut.dma_1.eq(int(image_1[y, x][i]))
                yield dut.dma_2.eq(int(image_2[y, x][i]))
                image_3[y, x][i] = yield dut.res_5
                yield
                print("{} {}".format('', (yield dut.res_5)))

dut = Math()
run_simulation(dut, pixel_processing(dut), vcd_name="result.vcd")
save_image()