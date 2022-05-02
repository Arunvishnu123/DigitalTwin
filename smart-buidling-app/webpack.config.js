const HtmlWebpackPlugin = require('html-webpack-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const webpack = require('webpack')
const path = require('path')
module.exports = {
    resolve: {
        alias: {
            '@': path.resolve('resources/js')
        }
    },
    entry: './src/main.js',
    module: {
        rules: [
            { test: /\.js$/, use: 'babel-loader' },
            { test: /\.vue$/, use: 'vue-loader' },
            { test: /\.css$/, use: ['vue-style-loader', 'css-loader'] },
            
        ]
    },
    devServer: {
        // open: true, // open browser after serve.
        hot: true,
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html',
        }),
        new VueLoaderPlugin(),
        
    ],
    node: {
        fs: 'empty'
    },
        devtool: "source-map",


}

