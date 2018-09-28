import HistoryMatching from './history_matching'

const global = window || {}

global.initHistoryMatch = function initHistoryMatch(
    elementSelector,
    data
) {
    const height = 800

    let visualization = new HistoryMatching()

    visualization.init(elementSelector, data)
}
