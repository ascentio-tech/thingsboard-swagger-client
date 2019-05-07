SWAGGER_VERSION=3.0.8
swagger-codegen-cli.jar:
	wget http://central.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/${SWAGGER_VERSION}/swagger-codegen-cli-${SWAGGER_VERSION}.jar -O swagger-codegen-cli.jar

THINGSBOARD_VERSION=2.3.0
clean-generated:
	rm -rf docs thingsboard_client
clean:
	rm -rf dist
.PHONY: clean clean-generated

generate-swagger-client: swagger-codegen-cli.jar clean-generated
	java -jar swagger-codegen-cli.jar generate -i swagger/thingsboard.json -l python -o . \
    --additional-properties projectName=thingsboard-client,packageName=thingsboard_client,packageVersion=${THINGSBOARD_VERSION},appDescription='Thingsboard REST client (auto-generated from Swagger spec)'

dist/thingsboard-client-${THINGSBOARD_VERSION}.tar.gz:
	python setup.py sdist

install-swagger-client: dist/thingsboard-client-${THINGSBOARD_VERSION}.tar.gz
	pip install dist/*${THINGSBOARD_VERSION}.tar.gz

