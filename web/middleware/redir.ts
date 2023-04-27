import { Middleware } from '@nuxt/types'

const noIndexMiddleware: Middleware = (context) => {
	context.redirect('/home')
}

export default noIndexMiddleware
