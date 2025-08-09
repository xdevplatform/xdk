import { defineConfig } from 'tsup';

export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: false, // Temporarily disabled to get working build
  splitting: false,
  sourcemap: true,
  clean: true,
  treeshake: true,
  minify: false,
  target: 'es2022',
  noExternal: ['node-fetch'],
  esbuildOptions(options) {
    options.resolveExtensions = ['.ts', '.js', '.tsx', '.jsx'];
  },
}); 