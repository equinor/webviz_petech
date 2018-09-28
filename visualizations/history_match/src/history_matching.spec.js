import HistoryMatching from './history_matching';
import chai from 'chai';
import sinonChai from 'sinon-chai';
chai.use(sinonChai);
import { expect } from 'chai';
import sinon from 'sinon';
import jsdom from 'jsdom-global';

describe('HistoryMatching', () => {
    beforeEach(() => {
        jsdom(
            `<body>
                <div id="history_matching_element">
                </div>
            </body>
        `);
    });

    describe('init', () => {
        it('should initialize the visualisation component', () => {
            let plot = new HistoryMatching();
            const data = {
                iterations: [{
                    positive: [],
                    negative: [],
                    labels: []
                }],
                confidence_interval_unsorted: { high: 0, low: 0 },
                confidence_interval_sorted: { high: [], low: []}
            }

            let spy = sinon.spy(plot, 'initVisualisation');

            plot.init("#history_matching_element", data);

            expect(spy).to.be.called;
        });

        it('should initialize the iteration picker component', () => {
            let plot = new HistoryMatching();
            const data = {
                iterations: [{
                    positive: [],
                    negative: [],
                    labels: []
                }],
                confidence_interval_unsorted: { high: 0, low: 0 },
                confidence_interval_sorted: { high: [], low: []}
            }

            let spy = sinon.spy(plot, 'initIterationPicker');

            plot.init("#history_matching_element", data);

            expect(spy).to.be.called;
        });
    });
});

