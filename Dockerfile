# Build stage
FROM python:alpine as builder
COPY . ./src/
WORKDIR /src/
RUN python3 -m pip install -r requirements.txt && \
    python3 -m build

# Distribution stage
FROM scratch
COPY --from=builder /src/dist/ /dist/