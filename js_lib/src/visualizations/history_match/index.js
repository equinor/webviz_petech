import HistoryMatching from './history_matching'

export function initHistoryMatch(
    elementSelector,
    data,
) {
    const height = 800

    const visualization = new HistoryMatching()

    visualization.init(elementSelector, data)
}
