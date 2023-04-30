<template lang="pug">
div(class='flex justify-center pt-4 space-x-2')
	a(href="/home")
		svg(
			class='w-6 h-6 text-gray-600 hover:text-green-300'
			aria-hidden='true'
			fill='none'
			stroke='currentColor'
			stroke-width='1.5'
			viewbox='0 0 24 24'
			xmlns='http://www.w3.org/2000/svg')
			path(
				d='M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25'
				stroke-linecap='round'
				stroke-linejoin='round')

	a(href='/about')
		svg(
			class='w-6 h-6 text-gray-600 hover:text-green-300'
			aria-hidden='true'
			fill='none'
			stroke='currentColor'
			stroke-width='1.5'
			viewbox='0 0 24 24'
			xmlns='http://www.w3.org/2000/svg')
			path(
				d='M14.25 9.75L16.5 12l-2.25 2.25m-4.5 0L7.5 12l2.25-2.25M6 20.25h12A2.25 2.25 0 0020.25 18V6A2.25 2.25 0 0018 3.75H6A2.25 2.25 0 003.75 6v12A2.25 2.25 0 006 20.25z'
				stroke-linecap='round'
				stroke-linejoin='round')

	a(href='https://github.com/syfqpie/salat' target='_blank')
		svg(
			class='w-6 h-6 text-gray-600 hover:text-green-300'
			xmlns='http://www.w3.org/2000/svg'
			xmlns:xlink='http://www.w3.org/1999/xlink'
			aria-hidden='true'
			role='img'
			width='32'
			height='32'
			preserveaspectratio='xMidYMid meet'
			viewbox='0 0 24 24')
			path(
				d='M12 2.247a10 10 0 0 0-3.162 19.487c.5.088.687-.212.687-.475c0-.237-.012-1.025-.012-1.862c-2.513.462-3.163-.613-3.363-1.175a3.636 3.636 0 0 0-1.025-1.413c-.35-.187-.85-.65-.013-.662a2.001 2.001 0 0 1 1.538 1.025a2.137 2.137 0 0 0 2.912.825a2.104 2.104 0 0 1 .638-1.338c-2.225-.25-4.55-1.112-4.55-4.937a3.892 3.892 0 0 1 1.025-2.688a3.594 3.594 0 0 1 .1-2.65s.837-.262 2.75 1.025a9.427 9.427 0 0 1 5 0c1.912-1.3 2.75-1.025 2.75-1.025a3.593 3.593 0 0 1 .1 2.65a3.869 3.869 0 0 1 1.025 2.688c0 3.837-2.338 4.687-4.563 4.937a2.368 2.368 0 0 1 .675 1.85c0 1.338-.012 2.413-.012 2.75c0 .263.187.575.687.475A10.005 10.005 0 0 0 12 2.247z'
				fill='currentColor')
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'LayoutFooter'
})
</script>
