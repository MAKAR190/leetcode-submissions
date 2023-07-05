function findWinners(matches: number[][]): number[][] {
   const players = new Map();
   let losers = [];
   let winners = [];
   for (let i = 0; i < matches.length; i++) {
       const loser = matches[i][1]
       const winner = matches[i][0]

       players.set(loser, (players.get(loser) + 1 || 1));
       players.set(winner, (players.get(winner) && players.get(winner) !== 0 ? players.get(winner) : 0));

   } 
    for (const [key, value] of players){
        if (value === 1){
            losers.push(key);
        } else if(value === 0){
            winners.push(key);
        }
    }
    return [winners.sort((a,b)=> a - b), losers.sort((a,b)=> a - b)]
};
