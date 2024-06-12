const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");
const app = express();

app.get("*", (req, res, next) => {
	console.log("GET", req.url);
	if (req.headers.authorization == "Bearer lm-studio") {
		next();
	}
});
app.post("*", (req, res, next) => {
	console.log("POST", req.url);
	if (req.headers.authorization == "Bearer lm-studio") {
		next();
	}
});
app.get(
	"*",
	createProxyMiddleware({
		target: "http://localhost:1234",
		changeOrigin: true,
	})
);
app.post(
	"*",
	createProxyMiddleware({
		target: "http://localhost:1234",
		changeOrigin: true,
	})
);

app.listen(1235, () => {
	console.log("Started proxy");
});
