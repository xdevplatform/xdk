import { defineConfig } from 'tsup';

export default defineConfig({
    entry: ['src/index.ts'],
    format: ['esm', 'cjs'],
    target: 'es2022',
    splitting: false,
    sourcemap: true,
    clean: true,
    dts: true,
    minify: true,
    treeshake: true,
    metafile: true,
    outDir: 'dist',
    outExtension({ format }) {
        return {
            js: format === 'cjs' ? '.cjs' : '.js',
        };
    },
}); 