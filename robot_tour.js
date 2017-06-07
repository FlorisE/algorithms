
var points = [
	['a', 0, 0],
	['b', 0, 5],
	['c', 5, 5],
	['d', 5, 0],
	['e', 0, 10],
	['f', 5, 10],
	['g', 10, 10],
	['h', 10, 0],
	['i', 10, 5],
	['j', 0, 15],
	['k', 5, 15],
	['l', 10, 15],
	['m', 15, 15]
];

function explore(s, unexplored, path, score) {
	//console.log(s, unexplored, path, score);
	if (unexplored.length == 0) {
		return [score, path];
	}
	
	var min = [99999, []];
	unexplored.forEach((s2) => {
		substractBFromA(unexplored, s2);
		var pathCopy = Array.from(path);
		pathCopy.push(s2);
		[score, path] = explore(s2, Array.from(unexplored), pathCopy, score+distance(s, s2));
		if (score < min[0]) {
			min = [score, path];
		}
	});
	return min;
}

function substractBFromA(list, item) {
	var index = list.findIndex((listitem) => listitem[0] == item[0]);
	list.splice(index, 1);
}

function distance(a, b) {
	var pointA = points.find((point) => point[0] == a);
	var pointB = points.find((point) => point[0] == b);
	return Math.sqrt(Math.pow(Math.abs(pointA[1]-pointB[1]), 2)+Math.pow(Math.abs(pointA[2]-pointB[2]), 2));
}


var start = points.map((point) => point[0]);

var min = [99999, []];
start.forEach((point, index) => {
	var unexplored = Array.from(start);
	unexplored.splice(index, 1);
	[score, path] = explore(point, unexplored, [point], 0);
	if (score < min[0]) {
		min = [score, path];
	}
});


console.log(score, path);
