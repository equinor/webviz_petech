import * as d3 from 'd3';
import Component from './component';

export default class Legend {
    constructor(config = {}) {
        this.validate(config);

        this.parentElement = config.parentElement;
        this.width = config.width ? config.width : 200;
        this.height = config.height ? config.height : 100;
        this.position = config.position ? config.position : { x: 0, y: 0 };
        this.data = [];
    }

    validate(config) {
        if (!config.parentElement) {
            throw new Error('Parent element not provided');
        }
    }

    loadData(data) {
        this.data = data;

        if (this.container) {
            this.renderLegend();
        }
    }

    render() {
        this.renderContainer();
        this.renderLegend();
    }

    renderContainer() {
        this.container = this.parentElement.append("g")
            .attr("id", "g_legend")
            .attr("transform", "translate(" + this.position.x + "," + this.position.y + ")");

        this.container
            .append("rect")
            .attr("width", this.width)
            .attr("height", this.height)
            .attr("x", 0)
            .attr("y", 0)
            .attr("fill", "white")
            .attr("fill-opacity", 0.9)
            .attr("stroke", "black");
    }

    renderLegend() {
        this._renderColourBoxes();
        this._renderLegendLabels();
    }

    _renderColourBoxes() {
        let colourBoxSelection = this.container
            .selectAll('rect.colorBox')
            .data(this.data);

        colourBoxSelection
            .exit()
            .remove();

        colourBoxSelection
            .enter()
            .append('rect')
            .attr('class', 'colorBox')
            .attr("width", 13.5)
            .attr("height", 13.5)
            .attr("x", 9)
            .attr("y", (d, i) => 9 + i * 22)
          .merge(colourBoxSelection)
            .attr("fill", (d) => d.box.colour)
            .attr("stroke", (d) => d.box.stroke)
            .attr("fill-opacity", (d) => d.box.fillOpacity);
    }

    _renderLegendLabels() {
        let legendTextSelection = this.container
            .selectAll('text.legendLabel')
            .data(this.data);

        legendTextSelection
            .exit()
            .remove();

        legendTextSelection
            .data(this.data)
            .enter()
            .append('text')
            .attr('class', 'legendLabel')
            .attr("x", 36)
            .attr("y", (d, i) => (i + 1) * 22)
            .attr("font-size", 20)
          .merge(legendTextSelection)
            .text((d) => d.label)
            .exit().remove();
    }
}
