// Generate UUID v4
function uuidv4() {
	return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
		/[xy]/g,
		function (c) {
			var r = (Math.random() * 16) | 0,
				v = c == "x" ? r : (r & 0x3) | 0x8;
			return v.toString(16);
		}
	);
}

// Set the header automatically
pm.request.headers.upsert({
	key: "Idempotency-Key",
	value: uuidv4(),
});
