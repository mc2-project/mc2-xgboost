# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import remote_pb2 as remote__pb2


class RemoteStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.rpc_get_remote_report_with_pubkey_and_nonce = channel.unary_unary(
                '/remote.Remote/rpc_get_remote_report_with_pubkey_and_nonce',
                request_serializer=remote__pb2.Status.SerializeToString,
                response_deserializer=remote__pb2.Report.FromString,
                )
        self.rpc_add_client_key = channel.unary_unary(
                '/remote.Remote/rpc_add_client_key',
                request_serializer=remote__pb2.DataMetadata.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )
        self.rpc_add_client_key_with_certificate = channel.unary_unary(
                '/remote.Remote/rpc_add_client_key_with_certificate',
                request_serializer=remote__pb2.DataMetadata.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )
        self.rpc_get_enclave_symm_key = channel.unary_unary(
                '/remote.Remote/rpc_get_enclave_symm_key',
                request_serializer=remote__pb2.Name.SerializeToString,
                response_deserializer=remote__pb2.EnclaveKey.FromString,
                )
        self.rpc_XGDMatrixCreateFromEncryptedFile = channel.unary_unary(
                '/remote.Remote/rpc_XGDMatrixCreateFromEncryptedFile',
                request_serializer=remote__pb2.DMatrixAttrsRequest.SerializeToString,
                response_deserializer=remote__pb2.Name.FromString,
                )
        self.rpc_XGBoosterCreate = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterCreate',
                request_serializer=remote__pb2.BoosterAttrsRequest.SerializeToString,
                response_deserializer=remote__pb2.Name.FromString,
                )
        self.rpc_XGBoosterSetParam = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterSetParam',
                request_serializer=remote__pb2.BoosterParamRequest.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )
        self.rpc_XGBoosterUpdateOneIter = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterUpdateOneIter',
                request_serializer=remote__pb2.BoosterUpdateParamsRequest.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )
        self.rpc_XGBoosterPredict = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterPredict',
                request_serializer=remote__pb2.PredictParamsRequest.SerializeToString,
                response_deserializer=remote__pb2.Predictions.FromString,
                )
        self.rpc_XGBoosterSaveModel = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterSaveModel',
                request_serializer=remote__pb2.SaveModelParamsRequest.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )
        self.rpc_XGBoosterLoadModel = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterLoadModel',
                request_serializer=remote__pb2.LoadModelParamsRequest.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )
        self.rpc_XGBoosterDumpModelEx = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterDumpModelEx',
                request_serializer=remote__pb2.DumpModelParamsRequest.SerializeToString,
                response_deserializer=remote__pb2.Dump.FromString,
                )
        self.rpc_XGBoosterDumpModelExWithFeatures = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterDumpModelExWithFeatures',
                request_serializer=remote__pb2.DumpModelWithFeaturesParamsRequest.SerializeToString,
                response_deserializer=remote__pb2.Dump.FromString,
                )
        self.rpc_XGBoosterGetModelRaw = channel.unary_unary(
                '/remote.Remote/rpc_XGBoosterGetModelRaw',
                request_serializer=remote__pb2.ModelRawParamsRequest.SerializeToString,
                response_deserializer=remote__pb2.Dump.FromString,
                )
        self.rpc_XGDMatrixNumCol = channel.unary_unary(
                '/remote.Remote/rpc_XGDMatrixNumCol',
                request_serializer=remote__pb2.NumColRequest.SerializeToString,
                response_deserializer=remote__pb2.Integer.FromString,
                )
        self.rpc_XGDMatrixNumRow = channel.unary_unary(
                '/remote.Remote/rpc_XGDMatrixNumRow',
                request_serializer=remote__pb2.Name.SerializeToString,
                response_deserializer=remote__pb2.Integer.FromString,
                )
        self.rpc_RabitInit = channel.unary_unary(
                '/remote.Remote/rpc_RabitInit',
                request_serializer=remote__pb2.RabitParams.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )
        self.rpc_RabitFinalize = channel.unary_unary(
                '/remote.Remote/rpc_RabitFinalize',
                request_serializer=remote__pb2.RabitParams.SerializeToString,
                response_deserializer=remote__pb2.StatusMsg.FromString,
                )


class RemoteServicer(object):
    """Interface exported by the server.
    """

    def rpc_get_remote_report_with_pubkey_and_nonce(self, request, context):
        """Get attestation report
        Status is a just a dummy argument and won't be used by the server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_add_client_key(self, request, context):
        """Send symmetric key encrypted with enclave public key, signature
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_add_client_key_with_certificate(self, request, context):
        """Send symmetric key encrypted with enclave public key, signature, certificate
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_get_enclave_symm_key(self, request, context):
        """Get enclave's symmetric key, encypted with the client's symmetric key
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGDMatrixCreateFromEncryptedFile(self, request, context):
        """Send params of a DMatrix to the server for initialization
        Returns the name assigned to this DMatrix
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterCreate(self, request, context):
        """Send params of a Booster to the server for initialization 
        Returns the name assigned to this booster
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterSetParam(self, request, context):
        """Set booster parameters
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterUpdateOneIter(self, request, context):
        """Update the booster for one round
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterPredict(self, request, context):
        """Run predictions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterSaveModel(self, request, context):
        """Save model to a file on the server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterLoadModel(self, request, context):
        """Load model from file on the server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterDumpModelEx(self, request, context):
        """Dump model 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterDumpModelExWithFeatures(self, request, context):
        """Dump model with features
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGBoosterGetModelRaw(self, request, context):
        """Save model to buffer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGDMatrixNumCol(self, request, context):
        """Get number of columns in the DMatrix
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_XGDMatrixNumRow(self, request, context):
        """Get number of rows in the DMatrix
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_RabitInit(self, request, context):
        """Initialize Rabit
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_RabitFinalize(self, request, context):
        """Finalize Rabit
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'rpc_get_remote_report_with_pubkey_and_nonce': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_get_remote_report_with_pubkey_and_nonce,
                    request_deserializer=remote__pb2.Status.FromString,
                    response_serializer=remote__pb2.Report.SerializeToString,
            ),
            'rpc_add_client_key': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_add_client_key,
                    request_deserializer=remote__pb2.DataMetadata.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
            'rpc_add_client_key_with_certificate': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_add_client_key_with_certificate,
                    request_deserializer=remote__pb2.DataMetadata.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
            'rpc_get_enclave_symm_key': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_get_enclave_symm_key,
                    request_deserializer=remote__pb2.Name.FromString,
                    response_serializer=remote__pb2.EnclaveKey.SerializeToString,
            ),
            'rpc_XGDMatrixCreateFromEncryptedFile': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGDMatrixCreateFromEncryptedFile,
                    request_deserializer=remote__pb2.DMatrixAttrsRequest.FromString,
                    response_serializer=remote__pb2.Name.SerializeToString,
            ),
            'rpc_XGBoosterCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterCreate,
                    request_deserializer=remote__pb2.BoosterAttrsRequest.FromString,
                    response_serializer=remote__pb2.Name.SerializeToString,
            ),
            'rpc_XGBoosterSetParam': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterSetParam,
                    request_deserializer=remote__pb2.BoosterParamRequest.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
            'rpc_XGBoosterUpdateOneIter': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterUpdateOneIter,
                    request_deserializer=remote__pb2.BoosterUpdateParamsRequest.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
            'rpc_XGBoosterPredict': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterPredict,
                    request_deserializer=remote__pb2.PredictParamsRequest.FromString,
                    response_serializer=remote__pb2.Predictions.SerializeToString,
            ),
            'rpc_XGBoosterSaveModel': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterSaveModel,
                    request_deserializer=remote__pb2.SaveModelParamsRequest.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
            'rpc_XGBoosterLoadModel': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterLoadModel,
                    request_deserializer=remote__pb2.LoadModelParamsRequest.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
            'rpc_XGBoosterDumpModelEx': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterDumpModelEx,
                    request_deserializer=remote__pb2.DumpModelParamsRequest.FromString,
                    response_serializer=remote__pb2.Dump.SerializeToString,
            ),
            'rpc_XGBoosterDumpModelExWithFeatures': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterDumpModelExWithFeatures,
                    request_deserializer=remote__pb2.DumpModelWithFeaturesParamsRequest.FromString,
                    response_serializer=remote__pb2.Dump.SerializeToString,
            ),
            'rpc_XGBoosterGetModelRaw': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGBoosterGetModelRaw,
                    request_deserializer=remote__pb2.ModelRawParamsRequest.FromString,
                    response_serializer=remote__pb2.Dump.SerializeToString,
            ),
            'rpc_XGDMatrixNumCol': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGDMatrixNumCol,
                    request_deserializer=remote__pb2.NumColRequest.FromString,
                    response_serializer=remote__pb2.Integer.SerializeToString,
            ),
            'rpc_XGDMatrixNumRow': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_XGDMatrixNumRow,
                    request_deserializer=remote__pb2.Name.FromString,
                    response_serializer=remote__pb2.Integer.SerializeToString,
            ),
            'rpc_RabitInit': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_RabitInit,
                    request_deserializer=remote__pb2.RabitParams.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
            'rpc_RabitFinalize': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_RabitFinalize,
                    request_deserializer=remote__pb2.RabitParams.FromString,
                    response_serializer=remote__pb2.StatusMsg.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'remote.Remote', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Remote(object):
    """Interface exported by the server.
    """

    @staticmethod
    def rpc_get_remote_report_with_pubkey_and_nonce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_get_remote_report_with_pubkey_and_nonce',
            remote__pb2.Status.SerializeToString,
            remote__pb2.Report.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_add_client_key(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_add_client_key',
            remote__pb2.DataMetadata.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_add_client_key_with_certificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_add_client_key_with_certificate',
            remote__pb2.DataMetadata.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_get_enclave_symm_key(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_get_enclave_symm_key',
            remote__pb2.Name.SerializeToString,
            remote__pb2.EnclaveKey.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGDMatrixCreateFromEncryptedFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGDMatrixCreateFromEncryptedFile',
            remote__pb2.DMatrixAttrsRequest.SerializeToString,
            remote__pb2.Name.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterCreate',
            remote__pb2.BoosterAttrsRequest.SerializeToString,
            remote__pb2.Name.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterSetParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterSetParam',
            remote__pb2.BoosterParamRequest.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterUpdateOneIter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterUpdateOneIter',
            remote__pb2.BoosterUpdateParamsRequest.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterPredict',
            remote__pb2.PredictParamsRequest.SerializeToString,
            remote__pb2.Predictions.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterSaveModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterSaveModel',
            remote__pb2.SaveModelParamsRequest.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterLoadModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterLoadModel',
            remote__pb2.LoadModelParamsRequest.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterDumpModelEx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterDumpModelEx',
            remote__pb2.DumpModelParamsRequest.SerializeToString,
            remote__pb2.Dump.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterDumpModelExWithFeatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterDumpModelExWithFeatures',
            remote__pb2.DumpModelWithFeaturesParamsRequest.SerializeToString,
            remote__pb2.Dump.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGBoosterGetModelRaw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGBoosterGetModelRaw',
            remote__pb2.ModelRawParamsRequest.SerializeToString,
            remote__pb2.Dump.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGDMatrixNumCol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGDMatrixNumCol',
            remote__pb2.NumColRequest.SerializeToString,
            remote__pb2.Integer.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_XGDMatrixNumRow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_XGDMatrixNumRow',
            remote__pb2.Name.SerializeToString,
            remote__pb2.Integer.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_RabitInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_RabitInit',
            remote__pb2.RabitParams.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_RabitFinalize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.Remote/rpc_RabitFinalize',
            remote__pb2.RabitParams.SerializeToString,
            remote__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
