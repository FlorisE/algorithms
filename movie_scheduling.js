var movies = [
	["a", 0, 2],
	["b", 1, 2],
	["c", 1, 3],
	["d", 2, 3],
	["e", 2, 4],
	["f", 3, 5],
	["g", 4, 6],
	["h", 5, 6],
	["j", 6, 7],
	["k", 6, 8]
];

var values = [true, false];

var combinations = [[true], [false]];

for (i = 0; i < movies.length-1; i++) {
	combinations.forEach((combination) => {
		var copied = Array.from(combination);
		combination.push(true);
		copied.push(false);
		combinations.push(copied);
	});
}

//console.log(combinations);

function overlap(a, b) {
	startA = a[1];
	startB = b[1];
	endA = a[2];
	endB = b[2];
	return (startA > startB && startA < endB) ||
		(startB > startA && startB < endA) ||
		(endA > startB && endA < endB) ||
		(endB > startA && endB < endA)
}

var overlapping = combinations.map(() => false);

for (i = 0; i < combinations.length; i++) {
	breakToTop = false;
	for (j = 0; j < combinations[i].length; j++) {
		if (breakToTop) break;
		if (!combinations[i][j]) continue;
		for (k = 0; k < combinations[i].length; k++) {
			if (!combinations[i][k]) continue;
			if (k == j) continue;
			if (overlap(movies[j], movies[k])) {
				overlapping[i] = true;
				breakToTop = true;
				break;
			}
		}
	}
}

//console.log(overlapping);

var scores = [];

overlapping.forEach((overlaps, index) => {
	if (!overlaps) {
		var combination = combinations[index];
		var filtered = combination.filter((included) => included);
		scores.push([combination.map((combi, ind) => combi ? movies[ind][0] : null).filter((item) => item), filtered.length]);
	}	
});

console.log(scores);
