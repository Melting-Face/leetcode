/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let min_price = 10000;
    for (const price of prices) {
        if (price < min_price) {
            min_price = price;
            continue;
        }
        const tmp_profit = price - min_price;
        if (tmp_profit > profit) {
            profit = tmp_profit
        }
    }
    return profit
};