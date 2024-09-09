import datetime as dt
import plotly.graph_objects as go 

class CandlePlot:
    
    def __init__(self, df, candles = True):
        self.df_plot = df.copy()
        self.candles = candles
        self.create_candle_fig()


    def add_timestr(self):
        self.df_plot['sTime'] = [dt.datetime.strftime(x, "s%y-%m-%d %H:%M") for x in self.df_plot.time]

    def create_candle_fig(self):
        self.add_timestr()
        self.fig = go.Figure()
        if self.candles == True:
            self.fig.add_trace(go.Candlestick(
                x = self.df_plot.sTime,
                open = self.df_plot.mid_o,
                high = self.df_plot.mid_h,
                low = self.df_plot.mid_l,
                close = self.df_plot.mid_c,
                line = dict(width = 1), opacity = 1,
                increasing_fillcolor = '#24A068',
                decreasing_fillcolor = '#CC2E3C',
                increasing_line_color = '#2EC886',
                decreasing_line_color = '#FF3A4C',
                name = "Trend"
            ))

    



    def update_the_layout(self, width, height, nticks):
        self.fig.update_yaxes(
            gridcolor = "#1f292f"
        )

        self.fig.update_xaxes(
            gridcolor = "#1f292f",
            rangeslider = dict(visible = False), #turns off the range slider
            # rangebreaks = [
            #     dict(bounds = ['sat', 'mon'])
            # ],
            nticks = nticks,
            #type = "date"
        )

        self.fig.update_layout(
            width = width,
            height = height,
            margin = dict(l=10, r=10, b=10, t=10),
            paper_bgcolor="#2c303c",
            plot_bgcolor = "#2c303c",
            #font_color = "#e1e1e1",
            font = dict(size = 8, color = "#e1e1e1"),
            legend_title_text='Trend',
            showlegend = True
            
        )

    def add_traces(self, line_traces):
        for t in line_traces:
            self.fig.add_trace(go.Scatter(
                x = self.df_plot.sTime,
                y = self.df_plot[t],
                line=dict(width = 2),
                line_shape="spline", 
                # line_color="red",
                name=t,
                
            ))

    def show_plot(self, width = 800, height = 400, nticks = 5, line_traces = []):
        self.add_traces(line_traces)
        self.update_the_layout(width, height, nticks)
        self.fig.show()


