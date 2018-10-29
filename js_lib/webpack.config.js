const path = require("path");
const webpack = require("webpack");
const postcssAutoprefixer = require('autoprefixer');
const postcssNested = require('postcss-nested');

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
      rules: [
          {
              test: /\.css$/,
              use: [
                  {
                      loader: 'css-loader',
                      options: {
                          importLoaders: 1,
                      },
                  },
                  {
                      loader: 'postcss-loader',
                      options: {
                          plugins: [
                              postcssNested(),
                              postcssAutoprefixer({
                                  browsers: [
                                      'last 2 versions',
                                      'not ie < 12'
                                  ]
                              }),
                          ],
                      },
                  }
              ]
          },
      ]
  },
  externals: {
    d3: "d3",
    webviz_petech: "webviz_petech"
  }
};
