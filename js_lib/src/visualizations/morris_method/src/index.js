import * as d3 from 'd3'
import sensitivitySliderPlot from './sensitivity_slider_plot'

const global = window || {}

global.initMorrisMethod = function initMorrisMethod(
    elementSelector,
    output,
    parameters,
    parameterName,
) {
    output.time = output.forEach(d => { d.time = new Date(d.time) })

    const plot = sensitivitySliderPlot(d3.select(elementSelector), output, parameters, parameterName).draw()

    d3.select('.sensitivity-slider-plot__graph-container')
        .classed('col-xs-12 tour-step-1', true)

    d3.select('.sensitivity-slider-plot__slider-container')
        .classed('col-xs-12 tour-step-2', true)

    window.addEventListener('resize', () => {
        plot.onResize()
    })

    // let visualization = new HistoryMatching()
    // visualization.init(elementSelector, data)
}
