<template lang="pug">
a(class='flex justify-center pt-8 pb-2 sm:pt-0' href='/' target='_blank')
    img(
        class="h-16 w-auto"
        src="~/assets/icons/salat.png"
    )
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'LayoutHeader'
})
</script>
