class Chart:
    max_size = 10
    column_size = int(240 / max_size)
    chart_top = 63

    def __init__(self, display_height=135):
        self.height = display_height
        self.pieces = [0] * Chart.max_size

    def add(self, amount):
        self.pieces = self.pieces[1:Chart.max_size]
        self.pieces.append(amount)

    def render(self):
        for (i, v) in enumerate(self.pieces):
            x = i * Chart.column_size
            y = self.height - int((v * Chart.chart_top)/100)
            w = Chart.column_size
            h = self.height - y
            yield (x, y, w, h)

