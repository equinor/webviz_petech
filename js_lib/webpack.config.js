const path = require("path");
const webpack = require("webpack");

module.exports =  {
  entry: ["./src/webviz_petech.js"],
  output: {
    path: path.resolve(__dirname, "./build/"),
    publicPath : "/html_resources/js/",
    filename : "webviz_petech.js",
    library: "webviz_petech"
  },
  devtool: 'inline-source-map',
  devServer: {
    contentBase: [
                    path.join(__dirname, "src/webportal/www"),
                    path.join(__dirname, "examples/webportal_example")
                 ]
  },
  resolve: {
    modules: [
        path.resolve(__dirname, "src/webportal/lib"),
        path.resolve(__dirname, "node_modules")
    ]
  },
  module: {
    rules:[
            {
                test:/\.css$/,
                use:['style-loader','css-loader']
            }
          ]
  },
  externals: {
    webviz_petech: "webviz_petech"
  }
};
