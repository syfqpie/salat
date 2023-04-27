module.exports = {
	root: true,
	env: {
		browser: true,
		'jest/globals': true,
		node: true
	},
	extends: [
		'@nuxtjs/eslint-config-typescript',
		'plugin:nuxt/recommended'
	],
	plugins: [
		'jest'
	],
	// add your custom rules here
	rules: {
		indent: ['error', 'tab'],
		'no-tabs': ['error', { allowIndentationTabs: true }],
		'no-console': 'off',
		'object-curly-spacing': ['error', 'always'],
		'padded-blocks': [
			'error', { blocks: 'never' }
		],
		'vue/block-spacing': [
			'error', 'never'
		],
		'vue/html-closing-bracket-newline': ['error', {
			singleline: 'never',
			multiline: 'never'
		}],
		'vue/html-indent': ['error', 'tab'],
		'vue/html-self-closing': ['error', {
			html: {
				void: 'always',
				normal: 'never',
				component: 'always'
			}
		}],
		'vue/object-curly-spacing': ['error', 'always'],
		'vue/padding-line-between-blocks': ['error', 'always'],
		'vue/template-curly-spacing': ['error', 'always']
	}
}
