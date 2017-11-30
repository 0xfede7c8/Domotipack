#!/bin/bash
npm run build
rm -r ../backend/public
cp -r build ../backend/public
