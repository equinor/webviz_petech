import * as d3 from 'd3'
import HistoryMatchingPlot from './history_matching_plot'
import Slider from '../../components/slider'

export default class HistoryMatching {
    init(container, data) {
        this.container = container
        this.data = data

        this.initVisualisation()
        this.initIterationPicker()
        this.initPlot()
        this._reorderTooltipLegendElements()
    }

    initVisualisation() {
        this.margin = {
            left: 200, right: 100, bottom: 100, top: 100,
        }

        this.plotWidth = 1200 - this.margin.left - this.margin.right // width of plot area
        this.plotHeight = 20 * (this.data.iterations[0].labels.length + 1) // height of plot area

        this.svg = d3.select(this.container).append('svg')
            .attr('width', this.plotWidth + this.margin.left + this.margin.right)
            .attr('height', this.plotHeight + this.margin.top + this.margin.bottom)
    }

    initPlot() {
        this.plot = new HistoryMatchingPlot({
            parentElement: this.svg,
            width: this.plotWidth,
            height: this.plotHeight,
            position: {
                x: this.margin.left,
                y: this.margin.top,
            },
            confidenceIntervalUnsorted: this.data.confidence_interval_unsorted,
            confidenceIntervalSorted: this.data.confidence_interval_sorted,
        })

        this.plot.setData(this.data.iterations[0])

        this.plot.render()
    }

    initIterationPicker() {
        this.sliderContainer = this.svg.append('g')

        this.sliderContainer.attr('width', this.plotWidth).attr('height', 80)

        this.iterationPicker = new Slider({
            parentElement: this.sliderContainer,
            data: this.data.iterations.map(iteration => iteration.name),
            length: this.plotWidth,
            width: 80,
            position: {
                x: 200,
                y: 40,
            },
            numberOfVisibleTicks: this.data.iterations.length,
        })

        this.iterationPicker.on('change', (index) => {
            this._setIteration(index)
        })

        this.iterationPicker.render()
    }

    _setIteration(index) {
        this.plot.setData(this.data.iterations[index])
    }

    _reorderTooltipLegendElements() {
        this.svg.node().appendChild(this.svg.select('#g_tooltip').node())
    }
}
