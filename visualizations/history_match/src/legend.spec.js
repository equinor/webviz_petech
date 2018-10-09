import Legend from './legend';
import chai from 'chai';
import sinonChai from 'sinon-chai';
chai.use(sinonChai);
import sinon from 'sinon';
import jsdom from 'jsdom-global';
import * as d3 from 'd3';

const { expect } = chai


describe('Legend component', () => {
    beforeEach(() => {
        jsdom(
            `<body>
            </body>
        `);
    });

    let createValidLegend = () => {
        let svg = d3.select('body').append('svg');

        let legend = new Legend({
            parentElement: svg
        });

        return legend;
    };

    describe('constructor', () => {
        it('should validate the config', () => {
            let spy = sinon.spy(Legend.prototype, 'validate');

            let legend = createValidLegend();

            expect(spy).to.be.called;
        });
    });


    describe('validate', () => {
        it('should throw an error if svg element is not provided', () => {
            let invalidLegendConstruction = () => {
                let legend = new Legend();
            };

            expect(invalidLegendConstruction).to.throw('Parent element not provided');
        });
    });

    describe('render', () => {
        it('should render the container element', () => {
            let legend = createValidLegend();

            let spy = sinon.spy(legend, 'renderContainer');

            legend.render();

            expect(spy).to.be.called;
        });

        it('should render the legend element', () => {
            let legend = createValidLegend();

            let spy = sinon.spy(legend, 'renderLegend');

            legend.render();

            expect(spy).to.be.called;
        });
    });

    describe('loadData', () => {
        it('should set the data property', () => {
            let legend = createValidLegend();
            let data = [
                {
                    label: 'Simulated values too high',
                    box: {
                        colour: '#34A037',
                        stroke: '#050',
                        fillOpacity: 0.7
                    }
                }
            ];

            legend.loadData(data);

            expect(legend.data).to.deep.equal(data);
        });

        it('should not render the legend if legend wasnt rendered before', () => {
            let legend = createValidLegend();
            let data = [
                {
                    label: 'Simulated values too high',
                    box: {
                        colour: '#34A037',
                        stroke: '#050',
                        fillOpacity: 0.7
                    }
                }
            ];
            let spy = sinon.spy(legend, 'renderLegend');

            legend.loadData(data);

            expect(spy).not.to.be.called;
        });

        it('should not render the legend if legend wasnt rendered before', () => {
            let legend = createValidLegend();
            let data = [
                {
                    label: 'Simulated values too high',
                    box: {
                        colour: '#34A037',
                        stroke: '#050',
                        fillOpacity: 0.7
                    }
                }
            ];

            legend.render();

            let spy = sinon.spy(legend, 'renderLegend');

            legend.loadData(data);

            expect(spy).to.be.called;
        });
    });
});

