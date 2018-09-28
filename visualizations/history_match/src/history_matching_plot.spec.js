import HistoryMatchingPlot from './history_matching_plot';
import * as d3 from 'd3';
import chai from 'chai';
import sinonChai from 'sinon-chai';
chai.use(sinonChai);
import { expect } from 'chai';
import sinon from 'sinon';
import jsdom from 'jsdom-global';

describe('History Matching Plot', () => {
    beforeEach(() => {
        jsdom(
            `<body>
                <div id="history_matching">
                </div>
            </body>
        `);
    });

    let createValidPlot = () => {
        return new HistoryMatchingPlot({
            parentElement: d3.select('body').append('svg'),
            confidenceIntervalUnsorted: { high: 0, low: 0 },
            confidenceIntervalSorted: { high: [], low: []}
        });
    }

    describe('constructor', () => {
        it('should validate the config', () => {
            let spy = sinon.spy(HistoryMatchingPlot.prototype, 'validate');

            let plot = createValidPlot();

            expect(spy).to.be.called;
        });
    });

    describe('validate', () => {
        it('should throw an error if svg element is not provided', () => {
            let invalidPlotConstruction = () => {
                let plot = new HistoryMatchingPlot();
            };

            expect(invalidPlotConstruction).to.throw('Parent element not provided');
        });
    });

    describe('setData', () => {
        it('should set the data property', () => {
            let plot = createValidPlot();
            let data = [{
                positive: [],
                negative: [],
                labels: [],
            }];

            plot.setData(data);

            expect(plot.data).to.deep.equal(data);
        });
    });

    describe('render', () => {
        it('should render the container element', () => {
            let plot = createValidPlot();

            let spy = sinon.spy(plot, 'renderContainer');

            plot.render();

            expect(spy).to.be.called;
        });

        it('should render the plot element', () => {
            let plot = createValidPlot();

            let spy = sinon.spy(plot, 'renderPlot');

            plot.render();

            expect(spy).to.be.called;
        });
    });
});

